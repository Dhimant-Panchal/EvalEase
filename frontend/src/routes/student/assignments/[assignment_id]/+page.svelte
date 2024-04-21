<script lang="ts">
    import { Button, Column, Grid, Row, Tile } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import KeywordEntry from "$lib/KeywordEntry.svelte";
    import { arraysEqual } from "$lib/ArrayUtils";

    export let data: PageData;
    let selection = data.keywords;
    $: unsaved = !arraysEqual(data.keywords, selection);

    const saveKeywords = () => {
        fetch("", {
            method: "POST",
            body: JSON.stringify({ keywords: selection }),
        });
        data.keywords = selection;
    };
</script>

<Grid>
    <Row>
        <Column>
            <h1>Submission</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Edit and view information associated with your submission.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <Tile style="margin-bottom: var(--cds-layout-01)">
                <h6 style="margin-bottom: var(--cds-layout-01)">Examiners</h6>
                <span style="display:block; margin-bottom: var(--cds-layout-01)">
                    Currently, no examiners have been assigned to this
                    submission.
                </span>
            </Tile>
            <Tile style="margin-bottom: var(--cds-layout-01)">
                <h6 style="margin-bottom: var(--cds-layout-01)">Keywords</h6>
                <span style="display:block; margin-bottom: var(--cds-layout-01)">
                    Keywords inform the matching process. A careful, pertinent
                    selection will help ensure your examiners are experienced in
                    your subject area.
                </span>
                <KeywordEntry bind:selection />
                <Button
                    style="margin-top: var(--cds-layout-01)"
                    type="submit"
                    disabled={!unsaved}
                    on:click={saveKeywords}
                >
                    Apply
                </Button>
            </Tile>
        </Column>
    </Row>
</Grid>
