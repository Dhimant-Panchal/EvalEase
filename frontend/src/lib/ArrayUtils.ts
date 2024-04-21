export function arraysEqual(a: string[], b: string[]) {
    return a.length === b.length && a.every((v, i) => v === b[i])
}