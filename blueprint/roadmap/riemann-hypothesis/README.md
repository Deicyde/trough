# Riemann Hypothesis (Alpöge)

Lean source that claims proofs of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, announced by Alpöge on 2026-11-20 in [a note](https://alpo.ge/remark.pdf). [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis) holds the published source under `src/`, unchanged, with the files a [Comparator](https://github.com/leanprover/comparator) check needs. This chapter reads it at commit [8ec38f92](https://github.com/leanprover-community/riemann-hypothesis/tree/8ec38f92ac54b5c91bc07f4f6f88ea61691b7975), of 2026-11-21.

The theorem pages show each statement as formalized and no proof, because no passing Comparator run on this source has been recorded; the people checking it keep [notes](https://github.com/leanprover-community/riemann-hypothesis/blob/8ec38f92ac54b5c91bc07f4f6f88ea61691b7975/verification/NOTES.md) in the repository.

The source has no license, so this chapter gives names, counts and links, and quotes none of its text.

`src/` holds 175,187 `.lean` files of the submission, leaving out Comparator's `Challenge.lean`: 17,374,215 lines, 15,531,759 of them non-blank, and 1,030,531,854 bytes. A line scan counts 818,755 `theorem` or `lemma` declarations and 242,670 by `def`, `abbrev`, `structure`, `class`, `instance` or `inductive`. It builds on Lean `v4.33.1` and Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

A line scan of every file finds no `sorry`, `admit`, `axiom` declaration, `native_decide`, `skipKernelTC`, `unsafe`, `opaque`, `implemented_by`, `extern` or `debug` option. It finds `addDecl` on 2 lines in 1 file, `modifyEnv` on 5 lines in 5 files, `run_tac` on 32 lines in 16 files, `kexactB` on 278 lines in 50 files, `kcopy` on 7 lines in 4 files and `allowUnsafeReducibility` on 37 lines in 33 files. `kexactB` and `kcopy` are tactics defined in the source that close a goal with a term whose type the elaborator does not compare with it, so for those proofs only the kernel's check applies.

Comparator's configuration names the five theorems below and permits the axioms `propext`, `Quot.sound` and `Classical.choice`.

## Claimed theorems

The five theorems Comparator's configuration names, in [src/Main.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/8ec38f92ac54b5c91bc07f4f6f88ea61691b7975/src/Main.lean).

- [riemannHypothesis](riemannhypothesis.md)
- [riemannZeta_eq_zero_re](riemannzeta-eq-zero-re.md)
- [LFunction_ne_zero_of_half_lt_re](lfunction-ne-zero-of-half-lt-re.md)
- [LFunction_eq_zero_re](lfunction-eq-zero-re.md)
- [LFunction_eq_zero_re_of_isPrimitive](lfunction-eq-zero-re-of-isprimitive.md)

## Folders

A page per top-level folder of `src/`, and a part per second-level folder of 300 files or more.

- [Main and Statements](main-and-statements/README.md)
- [BuildAid](buildaid/README.md)
- [CompanionTheory](companiontheory/README.md)
- [Development](development/README.md)
- [Formalism](formalism/README.md)
- [GroundTheory](groundtheory/README.md)
- [Lemmata](lemmata/README.md)
- [PositivityTheory](positivitytheory/README.md)
- [ReciprocityTheory](reciprocitytheory/README.md)
- [Supplements](supplements/README.md)
