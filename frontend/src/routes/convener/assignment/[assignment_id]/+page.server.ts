import type { AssignmentReport } from "$lib/ApiTypes";
import { getDjHeaders } from "$lib/Django";
import type { Actions, ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch, params }) => {
    const apiFetch = (path: string) => fetch(path, { headers: getDjHeaders(cookies) });

    const [submissions, report] = await Promise.all([
        apiFetch(`/api/convener/assignments/${params.assignment_id}/overview`).then(o => o.json()),
        apiFetch(`/api/convener/assignments/${params.assignment_id}/report`).then(o => o.json()),
    ])

    interface Submission {
        id: number;
        urn: number;
        marker_count: number;
    }

    return {
        report: report as AssignmentReport | undefined,
        submissions: submissions as Submission[],
    }
};