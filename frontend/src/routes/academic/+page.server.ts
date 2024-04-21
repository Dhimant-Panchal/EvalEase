import type { AcademicProfile, Evaluation } from "$lib/ApiTypes";
import { getDjHeaders } from "$lib/Django";
import type { Actions, ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch }) => {
    const [profile, inbox] = await Promise.all([
        fetch("/api/academic/myprofile", {
            headers: getDjHeaders(cookies)
        }).then(o => o.json()),
        fetch("/api/academic/inbox", {
            headers: getDjHeaders(cookies)
        }).then(o => o.json()),
    ])

    return {
        profile: profile as AcademicProfile,
        inbox: inbox as Evaluation[],
    }
};

export const actions = {
    updateinterests: async ({ cookies, request, fetch }) => {
        await fetch("/api/academic/myprofile", {
            headers: getDjHeaders(cookies),
            method: "PUT",
            body: await request.text(),
        })
    },
    submitevaluations: async ({ cookies, request, fetch }) => {
        const formData = await request.formData();

        const promises = [];

        formData.forEach((value, key) => {
            if (!value) return;
            promises.push(
                fetch(`/api/academic/submit/${key}`, {
                    headers: getDjHeaders(cookies),
                    method: "PUT",
                    body: String(value),
                })
            )
        })

        // await fetch("/api/academic/myprofile", {
        //     headers: getDjHeaders(cookies),
        //     method: "PUT",
        //     body: await request.text(),
        // })
    },
} satisfies Actions;