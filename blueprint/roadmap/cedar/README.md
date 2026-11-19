# Cedar: the Lean formalization of the Cedar policy language

[cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) says in its README:

> This repository contains the formalization of Cedar and infrastructure for performing differential randomized testing (DRT) between the formalization and Rust production implementation available in [`cedar`](https://github.com/cedar-policy/cedar).

Its Lean is the Lake project in `cedar-lean/`. The project's libraries other than `Cedar`, for Protobuf serialization, the foreign function interface and tests, are left out.

This chapter maps Cedar at commit [326d93c2](https://github.com/cedar-policy/cedar-spec/tree/326d93c24490c90607a3e257318e9c6a049c8116) (2026-11-18), with Lean toolchain v4.36.0. It has an article for each of the 287 modules under `cedar-lean/Cedar/` that declare something public by name, in a part per folder of `cedar-lean/Cedar/` and a page per folder below. They hold 3,905 public declarations, 2,553 theorems, 1,298 definitions and 54 instances and aliases, 971 of them with a docstring. The other 17 modules declare nothing public by name; they are listed on their folders' pages.

An article is titled by its module docstring, or by its file name when the docstring has no title; where modules share a title, each adds the shortest end of its path that tells them apart. It gives its docstrings and a block per public declaration in file order with its Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future work; an ellipsis marks each cut. No declaration's value holds `sorry`.

Edges come from Lean: a GitHub Actions run builds Cedar at this commit and reads, for each module, which other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a dependency reached through another is left out. That gives 465 statement edges and 340 proof edges. The same run checks the names read from the source: Lean marks 549 of them as private to their modules (in a `module` file, a declaration outside a `public section` and not marked `public` is private), and these are left out.

The docstrings, Lean statements and README text are quoted from [cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) at commit [326d93c2](https://github.com/cedar-policy/cedar-spec/tree/326d93c24490c90607a3e257318e9c6a049c8116), under its Apache-2.0 license.

These modules declare nothing public by name, so they have no article: [`Cedar.Data`](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data.lean), [`Cedar.Spec`](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec.lean), [`Cedar.TPE`](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE.lean), [`Cedar.Thm`](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm.lean) and [`Cedar.Validation`](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation.lean).

- [Data](data/README.md)
- [Slice](slice/README.md)
- [Spec](spec/README.md)
- [SymCC](symcc/README.md)
- [SymCCOpt](symccopt/README.md)
- [TPE](tpe/README.md)
- [Thm](thm/README.md)
- [Validation](validation/README.md)
- [SymCC](symcc-2.md)
- [SymCCOpt](symccopt-2.md)
