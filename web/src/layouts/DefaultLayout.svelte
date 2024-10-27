<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { DarkMode } from 'flowbite-svelte';
  import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from 'flowbite-svelte';
</script>
<div class="flex flex-col h-screen justify-between dark:bg-gray-800">
<Navbar>
  <DarkMode />
  <NavBrand href="/">
    <img src="/static/imgs/ClairvoyanceLogo.svg" class="me-3 h-6 sm:h-9" alt="Clairvoyance" />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Clairvoyance</span>
  </NavBrand>
  <NavHamburger  />
  <NavUl >
    <NavLi href="/">Home</NavLi>
    <NavLi href="/events">Events</NavLi>
  </NavUl>
</Navbar>

<div class="bg-white dark:bg-gray-800 dark:text-white mb-auto h-10">
    <div><slot></slot></div>
</div>

<Footer>
  <FooterCopyright href="/" by="Flowbite™" year={2022} />
  <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
    <FooterLink href="/">About</FooterLink>
    <FooterLink href="/">Privacy Policy</FooterLink>
    <FooterLink href="/">Licensing</FooterLink>
    <FooterLink href="/">Contact</FooterLink>
  </FooterLinkGroup>
</Footer>
</div>
