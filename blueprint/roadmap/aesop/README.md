# Aesop: proof search for Lean

[leanprover-community/aesop](https://github.com/leanprover-community/aesop) says in its README:

> Aesop (Automated Extensible Search for Obvious Proofs) is a proof search tactic for Lean 4. It is broadly similar to Isabelle's `auto`.

Mathlib requires it.

This chapter maps Aesop at commit [637fdbb8](https://github.com/leanprover-community/aesop/tree/637fdbb8689a3387a82568b07355231f892144d7) (2026-11-18), with Lean toolchain v4.37.0-rc1. It has an article for each of the 128 modules under `Aesop/` that declare something public by name, in a part per folder of `Aesop/` and a page per folder below. They hold 1,319 public declarations, 4 theorems, 1,314 definitions and 1 instance or alias, 219 of them with a docstring. The other 3 modules declare nothing public by name; they are listed on their folders' pages.

An article is titled by its module docstring, or by its file name when the docstring has no title; where modules share a title, each adds the shortest end of its path that tells them apart. It gives the module's authors as its header names them, its docstrings, and a block per public declaration in file order with its Lean statement: the text up to the `:=` or `where` that starts its value, or the whole text of a structure, class or inductive type. These are read from the source text, without Lean. Unnamed instances and the names an `alias ⟨…⟩` command gives are left out, and so are TODO notes and text about plans or inviting future work; an ellipsis marks each cut.

Edges come from Lean: a GitHub Actions run builds Aesop at this commit and reads, for each module, which other modules' declarations its own use. “Depends on” lists the modules its statements use, the types of its declarations and the values of its definitions, and “Proof depends on” those only its proofs use; a dependency reached through another is left out. That gives 213 statement edges and 20 proof edges. The same run checks the names read from the source: Lean marks 0 of them as private to their modules (in a `module` file, a declaration outside a `public section` and not marked `public` is private), and these are left out, as are 3 names Lean does not have.

The docstrings, Lean statements and README text are quoted from [leanprover-community/aesop](https://github.com/leanprover-community/aesop) at commit [637fdbb8](https://github.com/leanprover-community/aesop/tree/637fdbb8689a3387a82568b07355231f892144d7), under its Apache-2.0 license.

These modules declare nothing public by name, so they have no article: [`Aesop.Exception`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Exception.lean) and [`Aesop.Frontend`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend.lean).

6 modules under `Aesop/` did not build in the library's own build, so Lean could not read them and they have no article: [`Aesop.Builder`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder.lean), [`Aesop.Forward.CompleteMatchQueue`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/CompleteMatchQueue.lean), [`Aesop.Index.DiscrKeyConfig`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrKeyConfig.lean), [`Aesop.Options`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Options.lean), [`Aesop.RuleTac.FVarIdSubst`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/FVarIdSubst.lean) and [`Aesop.Tree`](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree.lean).

## [Builder to EMap](part-01/README.md)

- [Builder](part-01/builder/README.md)
- [BuiltinRules](part-01/builtinrules/README.md)
- [Forward](part-01/forward/README.md)
- [Frontend](part-01/frontend/README.md)
- [Index](part-01/index/README.md)
- [Options](part-01/options/README.md)
- [Rule](part-01/rule/README.md)
- [RulePattern](part-01/rulepattern/README.md)
- [RuleSet](part-01/ruleset/README.md)
- [RuleTac](part-01/ruletac/README.md)
- [Script](part-01/script/README.md)
- [Search](part-01/search/README.md)
- [Stats](part-01/stats/README.md)
- [Tree](part-01/tree/README.md)
- [Util](part-01/util/README.md)
- [BaseM](part-01/basem.md)
- [BuiltinRules](part-01/builtinrules-2.md)
- [Aesop/Check](part-01/check.md)
- [Constants](part-01/constants.md)
- [EMap](part-01/emap.md)

## [ElabM to Aesop/Tracing](part-02/README.md)

- [ElabM](part-02/elabm.md)
- [Index](part-02/index.md)
- [Aesop/Main](part-02/main.md)
- [Nanos](part-02/nanos.md)
- [Percent](part-02/percent.md)
- [Rule](part-02/rule.md)
- [Aesop/RulePattern](part-02/rulepattern.md)
- [RuleSet](part-02/ruleset.md)
- [RuleTac](part-02/ruletac.md)
- [Aesop/Saturate](part-02/saturate.md)
- [Aesop/Tracing](part-02/tracing.md)
