<script lang="ts">
    import { ClickableTile } from "carbon-components-svelte";

    interface Course {
        code: string;
        title: string;
    }

    export let courses: Course[] = [];
</script>

<div class="course-grid-wrapper">
    {#each courses as course}
        <ClickableTile href={`student/modules/${course.code}/`} data-sveltekit-preload-data="hover">
            <div class="course-tile-inner" style="position: relative;">
                <div style="display: block; position:absolute; bottom: 0px">
                    <h5>{course.code}</h5>
                    <h7>{course.title}</h7>
                </div>
            </div>
        </ClickableTile>
    {/each}
</div>

<style>
    .course-grid-wrapper {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: var(--cds-spacing-02);
    }

    .course-tile-inner {
        height: 200px;
    }

    @media (width <= 1200px) {
        .course-tile-inner {
            height: 140px;
        }
        .course-grid-wrapper {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media (width <= 600px) {
        .course-tile-inner {
            height: 40px;
        }
        .course-grid-wrapper {
            grid-template-columns: repeat(1, 1fr);
        }
    }
</style>
