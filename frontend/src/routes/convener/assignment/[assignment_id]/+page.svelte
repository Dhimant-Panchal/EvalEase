<script lang="ts">
    import {
        Button,
        Column,
        DataTable,
        Grid,
        Link,
        Row,
        Tile,
    } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import AcademicTileGrid from "$lib/AcademicTileGrid.svelte";

    export let data: PageData;
</script>

<Grid>
    <Row>
        <Column>
            <h1>Assignment</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Manage submissions for this assignment.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <Tile style="margin-bottom: var(--cds-layout-01)">
                <h6 style="margin-bottom: var(--cds-layout-01)">Report</h6>
                <span
                    style="display:block; margin-bottom: var(--cds-layout-01)"
                >
                    Statistics will appear here when at least 2 marks have been
                    received from academics.
                </span>
                <AcademicTileGrid>
                    {#if data.report?.all_mean}
                        <Tile light>
                            <p>
                                Mean Score: {data.report.all_mean.toFixed(2)}
                            </p>
                        </Tile>
                    {/if}
                    {#if data.report?.all_std_dev}
                        <Tile light>
                            <p>
                                Standard Deviation: {data.report.all_std_dev.toFixed(
                                    2,
                                )}
                            </p>
                        </Tile>
                    {/if}
                    {#each data.report?.outliers || [] as outlier}
                        <Tile light>
                            <p style="margin-bottom: var(--cds-layout-01)">
                                Outlier (URN {outlier.submission.urn})
                            </p>
                            <span
                                style="display:block; margin-bottom: var(--cds-layout-01)"
                            >
                                Scored {outlier.score} with {outlier.submission.marker_count} academic evaluations received
                            </span>
                            <Button href="/convener/submission/{outlier.submission.id}" kind="danger">
                                Manage
                            </Button>
                        </Tile>
                    {/each}
                </AcademicTileGrid>
            </Tile>
            <DataTable
                title="Submissions"
                description="These are the submissions for this assignment. Click one to manage its assigned markees."
                headers={[
                    { key: "urn", value: "Student URN" },
                    {
                        key: "returned_marks",
                        value: "Returned Evaluations Count",
                    },
                    { key: "marker_count", value: "Assigned Academics Count" },
                ]}
                sortKey="marker_count"
                sortDirection="ascending"
                rows={data.submissions}
            >
                <svelte:fragment slot="cell" let:row let:cell>
                    {#if cell.key === "urn"}
                        <Link href="/convener/submission/{row.id}"
                            >{cell.value}</Link
                        >
                    {:else}
                        {cell.display
                            ? cell.display(cell.value, row)
                            : cell.value}
                    {/if}
                </svelte:fragment>
            </DataTable>
        </Column>
    </Row>
</Grid>
