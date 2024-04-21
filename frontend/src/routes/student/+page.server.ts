import { getDjHeaders } from "$lib/Django";
import type { ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch }) => {
    const res = await fetch("/api/student/modules/", {
        headers: getDjHeaders(cookies)
    })

    interface Course {
        code: string;
        title: string;
    }

    return {
        courses: (await res.json()) as [Course]
    }
};