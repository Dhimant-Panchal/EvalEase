<script lang="ts">
    import type { PageData } from "./$types";
    import { enhance } from "$app/forms";

    import { Button, Tile } from "carbon-components-svelte";

    import KeywordList from "$lib/KeywordList.svelte";
    import AcademicTileGrid from "$lib/AcademicTileGrid.svelte";
    import Mast from "$lib/Mast.svelte";

    export let data: PageData;
</script>

<Mast
    title="URN {data.details.urn}'s Submission"
    strapline="Match examiners given this submission's submitted information."
>
    <Tile style="margin-bottom: var(--cds-layout-01)">
        <h6 style="margin-bottom: var(--cds-layout-01)">Keywords</h6>
        <span style="display:block; margin-bottom: var(--cds-layout-01)">
            Keywords are assigned by this submission's creator, informing the
            automatic work-academic pairing algorithm. You may also use this
            information to inform your decisions in manually assigning
            examiners.
        </span>
        <KeywordList selection={data.details.keywords} />
    </Tile>
    <Tile style="margin-bottom: var(--cds-layout-01)">
        <h6 style="margin-bottom: var(--cds-layout-01)">
            Reccomended Academics
        </h6>
        <span style="display:block; margin-bottom: var(--cds-layout-01)">
            Based on keywords, the following academics are reccomended for this
            submission.
        </span>
        <AcademicTileGrid>
            {#each data.reccomendations as rec}
                <Tile
                    light
                    style="display: flex; align-items:center; justify-content:space-between; min-height: 0px;"
                >
                    <span style="display: block;">
                        <h6 style="margin-bottom: var(--cds-spacing-02)">
                            {rec.academic.full_name}
                        </h6>
                        <span>
                            {rec.overlap} overlap{rec.overlap != 1 ? "s" : ""}
                        </span>
                    </span>
                    <form method="POST" action="?/addacademic" use:enhance>
                        <Button
                            name="target"
                            value={rec.academic.id}
                            type="submit"
                            disabled={data.evaluations.find(
                                (a) => a.marker == rec.academic.id,
                            ) != undefined}>Add</Button
                        >
                    </form>
                </Tile>
            {/each}
        </AcademicTileGrid>
    </Tile>
    <Tile>
        <h6 style="margin-bottom: var(--cds-layout-01)">Assigned Academics</h6>
        <span style="display:block; margin-bottom: var(--cds-layout-01)">
            The following academics are assigned to the submission.
        </span>
        <AcademicTileGrid>
            {#each data.evaluations as ev}
                <Tile light>
                    <h6>
                        {data.academics.find((o) => o.id == ev.marker)
                            ?.full_name}
                    </h6>
                    <span
                        style="display:block; margin-top: var(--cds-layout-01);"
                    >
                        {ev.mark
                            ? `Awarded ${ev.mark} marks`
                            : "Mark not yet received"}
                    </span>
                    <form method="POST" action="?/removeevaluation" use:enhance>
                        <Button
                            name="target"
                            style="margin-top: var(--cds-layout-01)"
                            kind="danger"
                            value={ev.id}
                            type="submit"
                        >
                            Remove Asignee
                        </Button>
                    </form>
                </Tile>
            {/each}
        </AcademicTileGrid>
    </Tile>
</Mast>
