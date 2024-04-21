<script lang="ts">
    import ModuleTile from "$lib/ModuleTile.svelte";
    import { Row, Column, Tile, Grid } from "carbon-components-svelte";
    import type { PageData } from "./$types";
    import CourseGrid from "$lib/CourseGrid.svelte";

    export let data: PageData;
</script>

<Grid>
    <Row>
        <Column>
            <h1>Student Home</h1>
            <p style="margin-bottom: var(--cds-layout-03)">
                Select a module below to view your assignments.
            </p>
        </Column>
    </Row>
    <Row>
        <Column>
            <CourseGrid courses={data.courses} />
        </Column>
    </Row>
</Grid>
