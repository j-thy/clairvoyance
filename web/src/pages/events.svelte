<script>
  import { router } from '@inertiajs/svelte'
	import { onMount } from 'svelte';
  import { inertia, Link } from '@inertiajs/svelte'
  import * as Table from "$lib/components/ui/table";
  import { Button } from "$lib/components/ui/button/index.js";
  import { toast } from "svelte-sonner";
  import * as Pagination from "$lib/components/ui/pagination";
  import ChevronLeft from "lucide-svelte/icons/chevron-left";
  import ChevronRight from "lucide-svelte/icons/chevron-right";

  // Get events from props
	let { events = undefined, num_pages = undefined } = $props();

  // Get current page number from URL
  const urlParams = new URLSearchParams(window.location.search);
  const isPageNum = urlParams.has('page');
  const parse_num = parseInt(urlParams.get('page'))
  let page_num = $state(isPageNum && !isNaN(parse_num) ? parse_num : 1);
  $inspect(page_num);

  // mounted() in VueJS / useEffect() in React
  onMount(() => {
    // We fire a partial reload to load the data in:
    // If events is undefined, we reload the page
    if (events === undefined) {
      router.reload({ only: ['events', 'num_pages'] })
      console.log("Mounted");
    }
  })

  const previous = () => {
    if (page_num > 0) {
      router.visit(`/events?page=${page_num}`, { only: ['events'] });
      console.log("Previous");
    }
    else {
      toast("You are at the first page")
    }
  };
  const next = () => {
    if (page_num <= num_pages) {
      router.visit(`/events?page=${page_num}`, { only: ['events'] });
      console.log("Next");
    }
    else {
      toast("You are at the last page")
    }
  };
  const gotoNum = () => {
    router.visit(`/events?page=${page_num}`);
    console.log("Goto2");
  };
</script>

<div class="relative flex min-h-screen flex-col dark">
  <Table.Root>
    <Table.Caption>Banner rateups.</Table.Caption>
    <a href="/events?page=1" use:inertia="{{ only: ['events'] }}">Show active</a>
    <Table.Header>
      <Table.Row>
        <Table.Head class="w-[100px]">Image</Table.Head>
        <Table.Head>Event</Table.Head>
        <Table.Head class="text-right">Region</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each events as event}
      <Table.Row>
        <Table.Cell><img src="/static/event_imgs/{event.image_file}" alt="sample 1" class="rounded-lg"></Table.Cell>
        <Table.Cell class="font-medium">{event.name}</Table.Cell>
        <Table.Cell class="text-right">{event.region}</Table.Cell>
      </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>

  <Pagination.Root bind:page={page_num} count={num_pages} perPage={1}>
    {#snippet children({ pages, currentPage })}
      {currentPage}
      <Pagination.Content>
        <Pagination.Item>
          <Pagination.PrevButton onclick={previous}>
            <ChevronLeft class="size-4" />
            <span class="hidden sm:block">Previous</span>
          </Pagination.PrevButton>
        </Pagination.Item>
        {#each pages as page (page.key)}
          {#if page.type === "ellipsis"}
            <Pagination.Item>
              <Pagination.Ellipsis />
            </Pagination.Item>
          {:else}
            <Pagination.Item>
              <Pagination.Link {page} onclick={gotoNum} isActive={currentPage === page.value}>
                {page.value}
              </Pagination.Link>
            </Pagination.Item>
          {/if}
        {/each}
        <Pagination.Item>
          <Pagination.NextButton onclick={next}>
            <span class="hidden sm:block">Next</span>
            <ChevronRight class="size-4" />
          </Pagination.NextButton>
        </Pagination.Item>
      </Pagination.Content>
    {/snippet}
  </Pagination.Root>
</div>
