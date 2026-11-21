# Batteries: the extended library for Lean

[leanprover-community/batteries](https://github.com/leanprover-community/batteries) says in its README:

> The "batteries included" extended library for Lean 4. This is a collection of data structures and tactics intended for use by both computer-science applications and mathematics applications of Lean 4.

Mathlib requires it, so every project built on Mathlib builds on it too.

This chapter maps Batteries at commit [e389e88a](https://github.com/leanprover-community/batteries/tree/e389e88a42889041c731d3aa86223f0ec70476a0) (2026-11-21), with Lean toolchain v4.37.0-rc1. It has an article for each of the 128 modules under `Batteries/` that declare something public by name, in a part per folder of `Batteries/` and a page per folder below. They hold 2,702 public declarations, 1,731 theorems, 958 definitions and 13 instances and aliases, 968 of them with a docstring. The other 61 modules declare nothing public by name, such as a module that only imports others, a deprecated module whose code has moved, or one that adds syntax or an elaborator; they are listed on their folders' pages.

An article is titled by its module docstring, or by its file name when the docstring has no title; where modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's authors as its header names them, its docstrings, and a block per public declaration in file order with its Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future work; an ellipsis marks each cut.

Edges come from Lean: a GitHub Actions run builds Batteries at this commit and reads, for each module, which other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a dependency reached through another is left out. That gives 63 statement edges and 23 proof edges. The same run checks the names read from the source: Lean marks 67 of them as private to their modules (in a `module` file, a declaration outside a `public section` and not marked `public` is private), and these are left out, as is 1 name Lean does not have.

The docstrings, Lean statements and README text are quoted from [leanprover-community/batteries](https://github.com/leanprover-community/batteries) at commit [e389e88a](https://github.com/leanprover-community/batteries/tree/e389e88a42889041c731d3aa86223f0ec70476a0), under its Apache-2.0 license.

These modules declare nothing public by name, so they have no article: [`Batteries.Recycling.MonadSatisfying`](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Recycling/MonadSatisfying.lean), [`Batteries.Recycling.RBTree`](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Recycling/RBTree.lean), [`Batteries.CodeAction`](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/CodeAction.lean) and [`Batteries.Linter`](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Linter.lean).

- [Classes](classes/README.md)
- [CodeAction](codeaction/README.md)
- [Control](control/README.md)
- [Data](data/README.md)
- [Lean](lean/README.md)
- [Linter](linter/README.md)
- [Tactic](tactic/README.md)
- [Util](util/README.md)
- [Logic](logic.md)
