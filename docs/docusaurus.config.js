// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'NightyLib',
  tagline: 'Your all-in-one OP utility for Nighty!',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  url: 'https://nightylib.bjarnos.dev',
  baseUrl: '/',
  organizationName: 'Bjarnos',
  projectName: 'NightyLib',
  onBrokenLinks: 'ignore',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/social-card.png',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'NightyLib',
        logo: {
          alt: 'NightyLib',
          src: 'img/NightyLib.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'docs',
            position: 'left',
            label: 'Documentation',
          },
          {to: '/about', label: 'About', position: 'left'},
          {
            href: 'https://nighty.one/',
            label: 'Nighty Official',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Community',
            items: [
              {
                label: 'Feature request',
                to: 'https://github.com/Bjarnos/NightyLib/issues',
              },
            ],
          },
          {
            title: 'Contact',
            items: [
              {
                label: 'Mail',
                href: 'mailto:contact@bjarnos.dev',
              },
              {
                label: 'Discord',
                href: 'https://discord.com/users/1146844311669981274',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'About',
                to: '/about',
              },
              {
                label: 'ToS',
                href: '/terms-of-service',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/Bjarnos/NightyLib',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear() === 2025 && 2025 || '2025-' + new Date().getFullYear()} Bjarnos & NightyLib Team. Website built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
