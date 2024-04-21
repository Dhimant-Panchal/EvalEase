import { getDjHeaders } from "$lib/Django";
import { type Actions, type ServerLoad, type Cookies } from "@sveltejs/kit";

function fetchSubmissionId(_fetch: typeof fetch, cookies: Cookies, params: Partial<Record<string, string>>) {
    return _fetch(`/api/student/assignments/${params.assignment_id}/submission`, {
        headers: getDjHeaders(cookies),
    }).then(a => a.text()).then(Number)
}

interface Submission {
    id: number;
    keywords: string[];
}

export const load: ServerLoad = async ({ cookies, params, fetch }) => {
    const submissionId = await fetchSubmissionId(fetch, cookies, params);
    const res = await fetch(`/api/student/submissions/${submissionId}/`, {
        headers: getDjHeaders(cookies),
    })
    return (await res.json()) as Submission
};

export const actions = {
    default: async ({ cookies, request, params, fetch }) => {
        const submissionId = await fetchSubmissionId(fetch, cookies, params);
        await fetch(`/api/student/submissions/${submissionId}/`, {
            headers: getDjHeaders(cookies),
            method: "PUT",
            body: await request.text(),
        })
    },
} satisfies Actions;