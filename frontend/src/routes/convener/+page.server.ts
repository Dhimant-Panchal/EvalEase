import { getDjHeaders } from "$lib/Django";
import type { Actions, ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch }) => {
    const assignments_res = await fetch("/api/convener/assignments", {
        headers: getDjHeaders(cookies)
    })

    interface Assignment {
        id: number;
        module: string;
        title: string;
        due_date: string;
    }

    return {
        assignments: (await assignments_res.json()) as Assignment[]
    }
};