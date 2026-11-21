# CompPoly: computable polynomials in Lean

[Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) says in its README:

> A formally verified library for computable polynomial operations over finite fields and general rings, supporting univariate, multivariate, multilinear, and bivariate polynomials.

This chapter maps CompPoly at commit [c72a7652](https://github.com/Verified-zkEVM/CompPoly/tree/c72a765272497b4c52201be11be47af5718c7488) (2026-11-20), with Lean toolchain v4.36.0 and Mathlib fc4f59e5. It has an article for each of the 362 modules under `CompPoly/` that declare something public by name, in a part per folder of `CompPoly/` and a page per folder below. They hold 7,346 public declarations, 4,454 theorems, 2,721 definitions and 171 instances and aliases, 4,035 of them with a docstring. The other 39 modules declare nothing public by name; they are listed on their folders' pages.

An article is titled by its module docstring, or by its file name when the docstring has no title; where modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's authors as its header names them, its docstrings, and a block per public declaration in file order with its Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future work; an ellipsis marks each cut. No declaration's value holds `sorry`.

Edges come from Lean: a GitHub Actions run builds CompPoly at this commit and reads, for each module, which other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a dependency reached through another is left out. That gives 497 statement edges and 182 proof edges. The same run checks the names read from the source, and Lean has each as a public declaration.

The docstrings, Lean statements and README text are quoted from [Verified-zkEVM/CompPoly](https://github.com/Verified-zkEVM/CompPoly) at commit [c72a7652](https://github.com/Verified-zkEVM/CompPoly/tree/c72a765272497b4c52201be11be47af5718c7488), under its Apache-2.0 license.

- [Bivariate](bivariate/README.md)
- [Data](data/README.md)
- [Fields](fields/README.md)
- [LinearAlgebra](linearalgebra/README.md)
- [Multilinear](multilinear/README.md)
- [Multivariate](multivariate/README.md)
- [ToMathlib](tomathlib/README.md)
- [Univariate](univariate/README.md)
