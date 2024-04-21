import type { AcademicProfile, AcademicReccomendation, Evaluation, SubmissionDetails } from "$lib/ApiTypes";
import { getDjHeaders } from "$lib/Django";
import type { Actions, ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch, params }) => {
    const apiFetch = (path: string) => fetch(path, { headers: getDjHeaders(cookies) });

    // https://kit.svelte.dev/docs/migrating-to-sveltekit-2#top-level-promises-are-no-longer-awaited
    const [evaluations, details, reccomendations] = await Promise.all([
        apiFetch(`/api/convener/submission/${params.submission_id}/evaluations`).then(o => o.json()),
        apiFetch(`/api/convener/submission/${params.submission_id}/details`).then(o => o.json()),
        apiFetch(`/api/convener/submission/${params.submission_id}/reccomendations`).then(o => o.json()),
    ])

    const academics = await Promise.all(
        (evaluations as Evaluation[]).map(a => apiFetch(`/api/academic/profiles/${a.marker}`).then(o => o.json()))
    )

    return {
        evaluations: evaluations as Evaluation[],
        details: details as SubmissionDetails,
        reccomendations: reccomendations as AcademicReccomendation[],
        academics: academics as AcademicProfile[],
    }
};

export const actions = {
    addacademic: async ({ cookies, request, fetch, params }) => {
        const formData = await request.formData();
        const academic_id = formData.get("target");

        const res = await fetch(`/api/convener/submission/${params.submission_id}/evaluations`, {
            headers: getDjHeaders(cookies),
            method: "POST",
            body: JSON.stringify({
                marker: academic_id,
                submission: params.submission_id,
            })
        })

        return { success: res.ok }
    },
    removeevaluation: async ({ cookies, request, fetch, params }) => {
        const formData = await request.formData();
        const evaluation_id = formData.get("target");

        const res = await fetch(`/api/convener/evaluation/${evaluation_id}`, {
            headers: getDjHeaders(cookies),
            method: "DELETE",
        })

        return { success: res.ok }
    },
} satisfies Actions;    