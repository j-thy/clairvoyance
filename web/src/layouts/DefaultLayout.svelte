<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { Button } from "$lib/components/ui/button";
  import { Toaster } from "$lib/components/ui/sonner/index.js";
</script>
<Toaster />
<div style="display: contents" class="relative flex min-h-screen flex-col">
  <Navbar class="dark:bg-transparent">
    <NavBrand href="/">
      <img src="/static/imgs/ClairvoyanceLogo.svg" class="me-3 h-6 sm:h-9" alt="Clairvoyance Logo" />
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Clairvoyance</span>
    </NavBrand>
    <NavHamburger  />
    <NavUl >
      <NavLi href="/">Home</NavLi>
      <NavLi href="/events">Events</NavLi>
      <NavLi href="/example">Example</NavLi>
    </NavUl>
  </Navbar>
  <slot></slot>
</div>