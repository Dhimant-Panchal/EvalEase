import { getDjHeaders } from "$lib/Django";
import { redirect, type ServerLoad } from "@sveltejs/kit";

export const load: ServerLoad = async ({ cookies, fetch }) => {
	const res = await fetch("/api/cworker/me/profiletype", {
		headers: getDjHeaders(cookies)
	})

	if (res.ok)
		redirect(307, `/${await res.json()}`)
	else
		redirect(307, "/auth")
};