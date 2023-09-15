# Turborepo, Next, and Django Starter with yarn

This repository contains a template for creating a turborepo using Next.js and Django. A turborepo is a monorepo that uses workspaces to manage multiple projects in a single repository. This makes it easier to share code and dependencies between projects, and it also makes it easier to manage updates to multiple projects at the same time.

This template includes everything you need to get started with a turborepo, including:
- A Next.js project for the front-end
- A Django project for the back-end
- A turborepo configuration file
- A README file with instructions on how to get started

## What's inside?

This Turborepo template uses [yarn](https://classic.yarnpkg.com/lang/en/) as a packages manager. It includes the following packages/apps:

### Apps and Packages

- `docs`: a [Next.js](https://nextjs.org/) app
- `web`: another [Next.js](https://nextjs.org/) app
- `shared`: a stub React component library which can be shared by all applications
- `ui`: a stub React component library shared by both `web` and `docs` applications
- `eslint-config-custom`: `eslint` configurations (includes `eslint-config-next` and `eslint-config-prettier`)
- `tsconfig`: `tsconfig.json`s used throughout the monorepo
- `backend`: a [Django](https://www.djangoproject.com/) app

### Setup

To install packages of every workspace
```
yarn install
```

### Utilities

This Turborepo has some additional tools already setup for you:

- [TypeScript](https://www.typescriptlang.org/) for static type checking
- [ESLint](https://eslint.org/) for code linting
- [Prettier](https://prettier.io) for code formatting
- [Django](https://www.djangoproject.com/) for django

### Build

To build all apps and packages, run the following command:

```
yarn build
```

### Develop (Front-end)

To develop all typescript apps and packages, run the following command:

```
yarn dev
```

To add packages:
```
yarn <workspace> add <package-name>
```

To remove packages:
```
yarn <workspace> remove <package-name>
```

### Develop (Django Back-end)

To develop django app, run the following:
```
yarn server
```

To make migrations:
```
yarn migrate:make
```

To show migrations:
```
yarn migrate:show
```

To apply migrations:
```
yarn migrate
```

To flush database:
```
yarn db:flush
```

### Remote Caching

Turborepo can use a technique known as [Remote Caching](https://turbo.build/repo/docs/core-concepts/remote-caching) to share cache artifacts across machines, enabling you to share build caches with your team and CI/CD pipelines.

By default, Turborepo will cache locally. To enable Remote Caching you will need an account with Vercel. If you don't have an account you can [create one](https://vercel.com/signup), then enter the following commands:

```
cd my-turborepo
npx turbo login
```

This will authenticate the Turborepo CLI with your [Vercel account](https://vercel.com/docs/concepts/personal-accounts/overview).

Next, you can link your Turborepo to your Remote Cache by running the following command from the root of your turborepo:

```
npx turbo link
```

## Useful Links

Learn more about the power of Turborepo:

- [Tasks](https://turbo.build/repo/docs/core-concepts/monorepos/running-tasks)
- [Caching](https://turbo.build/repo/docs/core-concepts/caching)
- [Remote Caching](https://turbo.build/repo/docs/core-concepts/remote-caching)
- [Filtering](https://turbo.build/repo/docs/core-concepts/monorepos/filtering)
- [Configuration Options](https://turbo.build/repo/docs/reference/configuration)
- [CLI Usage](https://turbo.build/repo/docs/reference/command-line-reference)
