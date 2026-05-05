# Contributing

There are multiple ways to contribute to the Plaice project, from using the system and filing
issues/features, to building new components to integrate with the system, to submitting pull
requests which edit the documentation or CAD files. Here, we only describe contributions
to the Plaice repository itself, not [interfacing components and/or remixes](/docs/design/InterfacingAndRemixing.md) with the core system.

## Preliminaries

Before contributing to this repository, make sure to do your research first to ensure that you don't expend unnecessary
effort. For example, if you have an apparent issue with the system, make sure that you've already looked through extant
issues to see if your discovery truly warrants a new issue, or if a "+1" or a comment on an existing issue would work better.
Similarly, before making any kind of contribution, it's strongly recommended to read through all relevant documentation on
Plaice [components](/docs/components/Index.md) and [design](/docs/design/Index.md) in the repository.

## Filing Issues

Mismatches between the documentation and the de facto behavior of Plaice, unsatisfying physical dilemmas in Plaice assemblies,
and problems with CAD or model files are all examples of potential subjects for GitHub issues. When filing an issue, make sure that
you've described the issue to the best of your ability -- if e.g: a picture can illustrate the issue effectively, please include one!

## Feature Requests

If there's some piece of documentation like a recipe which would be helpful/illuminating, a proposal for a new core Plaice component,
or an integration with another modular construction system, filing a feature request is a good choice. That said, given the nature
and goals of this project, feature requests will typically take longer to reach their ultimate resolution than issues. Plaice is
ultimately meant to be "energy-minimizing" in the sense that the set of core components is kept to only those components where there
can be near-universal agreement that the important aspects of those components are "correct" with respect to the structure of
the rest of the system. In practice, this means that proposals for new core components will require _lots_ of discussion and
potentially many back-and-forth revisions before a component is ready for inclusion in the core system. Depending on the motivation
and whether/not the component ultimately achieves the standard of "inevitability" applied to core Plaice components, a proposal
for inclusion in core may wind up being better-expressed as an external component which interfaces with the system instead. 

## Pull Requests

The Plaice repository consists of both documentation and CAD, each of which has different PR standards. That said, PRs should
only ever be done as a follow-up to an issue or feature request, whether for an effective demonstration of a prototype of a proposed change,
or to fully implement what was described (and discussed) in an issue. Ensure that your pull requests have a pithy commit message top-line,
but with sufficient detail in the body of the message to describe the gist of the change. Additionally, PRs which edit CAD files may also
need to update documentation for the change to land.

### Documentation
Since repo documentation is in Markdown, changes to docs are reviewable with standard diff tools. When reviewing documentation, grammatical
correctness, conciseness, and comprehensive coverage are all factors to consider. Additionally, documentation in this repository
should follow Wikipedia-style cross-linking rules -- i.e: the first time that a topic with another documentation page is mentioned
on a page, that mention (and that mention only) is the one that gets the link.

### CAD
CAD files in this repository are all FreeCAD files, which are internally .zipped bundles of XML and other files. while changes to these
files can provide a high-level summary of what parts of the Plaice repository were modified and some of the "how", the diffs are by
no means sufficient to describe the changes relative to patching down a PR and loading up the modified file(s) in FreeCAD. Consequently,
for PRs which modify CAD files, good commit messages are _critical_ for helping reviewers to get through reviews quickly. 

Additionally, there are several norms that we follow when it comes to the structure of CAD files in our repository -- most of these
are general best-practices for CAD (use of master sketches, data planes and other references, and a progression of part-design
features from the most topologically-stable ones to the least). While requests to adhere to these best-practices may feel like "bike-shedding",
it rarely is in an open-hardware project given the large potential for churn and the fundamental need to keep the modeling structure
comprehensible.

## Code of Conduct
In general, don't be an asshole. Racism, sexism, classism, homophobia, transphobia, and any other form of hate will not be tolerated,
as well as aggressive or harassing behaviors in PRs or in comments on issues. 

## Maintainers
The current maintainer of this repo is MycelialDesigns (me). I do not want to maintain this repository indefinitely, since I would
rather see this repository become community-maintained, and don't particularly think of myself of having the right set of personal attributes
for a long-term maintainer of a project. If you're enthusiastic about potentially becoming a maintainer, feel free to shoot a message my way!
However, be aware that any transition of this project to new maintainers will only happen when a sufficient level of condifdence has been
built -- e.g: by submitting particularly high-quality PRs or by having a large impact on the overall Plaice community.
