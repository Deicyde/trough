# CSLib: the Lean Computer Science Library

[leanprover/cslib](https://github.com/leanprover/cslib), the Lean Computer Science Library, says in its README:

> The Lean library for Computer Science.
>
> Official website at <https://www.cslib.io/>.
>
> …
>
> CSLib aims at formalising Computer Science theories and tools, broadly construed, in the Lean programming language.

Its GOVERNANCE.md names Fabrizio Montesi as lead maintainer, Alexandre Rademaker and Sorrachai Yingchareonthawornchai as technical leads and Ching-Tsun Chou, Chris Henson, Kim Morrison, Alexandre Rademaker, Samuel Schlesinger, Christian Reitwiessner, Thomas Waring and Sorrachai Yingchareonthawornchai as area maintainers.

This chapter maps CSLib at commit [86d560b6](https://github.com/leanprover/cslib/tree/86d560b6cbb379bd82512424cbcd2a915a1565e7) (2026-11-12), with Lean toolchain v4.36.0-rc2 and Mathlib 887bb849. It has an article for each of the 301 modules under `Cslib/`, in a part per folder of `Cslib/` and a page per folder below. They hold 4,408 public declarations, 2,969 theorems, 1,364 definitions and 75 instances and aliases, 3,032 of them with a docstring; 6 modules declare nothing public by name.

An article is titled by its module docstring, or by its file name when the docstring has no title; where modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's authors as its header names them, its docstrings, and a block per public declaration in file order with its Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future work; an ellipsis marks each cut. No declaration's value holds `sorry`.

Edges come from Lean: a GitHub Actions run builds CSLib at this commit and reads, for each module, which other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a dependency reached through another is left out. That gives 368 statement edges and 83 proof edges. The same run checks the names read from the source: Lean marks 59 of them as private to their modules (in a `module` file, a declaration outside a `public section` and not marked `public` is private), and these are left out.

The docstrings, Lean statements and README text are quoted from [leanprover/cslib](https://github.com/leanprover/cslib) at commit [86d560b6](https://github.com/leanprover/cslib/tree/86d560b6cbb379bd82512424cbcd2a915a1565e7), under its Apache-2.0 license.

- [Algorithms](algorithms/README.md)
- [Computability](computability/README.md)
- [Crypto](crypto/README.md)
- [Foundations](foundations/README.md)
- [Languages](languages/README.md)
- [Logics](logics/README.md)
- [MachineLearning](machinelearning/README.md)
- [Probability](probability/README.md)
- [Tactic](tactic/README.md)
- [CSLib Initialization](init.md)
