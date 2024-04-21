import type { ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, params, fetch }) => {
    const res = await fetch(`/api/student/modules/${params.module_id}/assignments/`, {
        headers: { "Authorization": `Token ${cookies.get("token")}` }
    })

    interface AssignmentResponse {
        id: number;
        title: string;
        due_date: string;
    }

    const data: AssignmentResponse[] = res.ok ? await res.json() : [];

    return {
        assignments: data.map(a => ({
            id: a.id,
            title: a.title,
            due_date: new Date(a.due_date)
        }))
    }
};