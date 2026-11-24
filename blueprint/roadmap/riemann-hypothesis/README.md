# Riemann Hypothesis (Alpöge)

Lean source that claims proofs of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, announced by Alpöge on 2026-11-20 in [a note](https://alpo.ge/remark.pdf). [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis) keeps the source under `src/`, with the files a [Comparator](https://github.com/leanprover/comparator) check needs. This chapter reads it at commit [2d0c622a](https://github.com/leanprover-community/riemann-hypothesis/tree/2d0c622a3464ba41ad98fca9086bab54fb74e303), of 2026-11-24. `src/` at this commit differs from [the source as published](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005), the repository's first commit, in 175,301 files (114 added, 114,671 removed and 60,516 changed; [compare](https://github.com/leanprover-community/riemann-hypothesis/compare/40e56bab0265...2d0c622a3464)). Of the two files that state the claimed theorems, `src/Main.lean` changed and `src/Challenge.lean` was added since then.

The theorem pages show each statement as formalized and no proof, because no passing Comparator run on this source has been recorded; the people checking it keep [notes](https://github.com/leanprover-community/riemann-hypothesis/blob/2d0c622a3464ba41ad98fca9086bab54fb74e303/verification/NOTES.md) in the repository.

The source has no license, so this chapter gives names, counts and links, and quotes none of its text.

`src/` holds 60,629 `.lean` files of the submission, leaving out Comparator's `Challenge.lean`: 16,766,464 lines, 15,011,469 of them non-blank, and 1,102,244,196 bytes. A line scan counts 612,095 `theorem` or `lemma` declarations and 166,666 by `def`, `abbrev`, `structure`, `class`, `instance` or `inductive`. It builds on Lean `v4.37.0-rc1` and Mathlib at [31ce06ea](https://github.com/leanprover-community/mathlib4/tree/31ce06eaadf4a200c0e1407c5f10953cf606b8f8).

A line scan of every file finds no `sorry`, `admit`, `axiom` declaration, `native_decide`, `skipKernelTC`, `unsafe`, `implemented_by`, `extern`, `debug` option, `addDecl`, `modifyEnv`, `kexactB` or `kcopy`. It finds `opaque` on 1 line in 1 file, `run_tac` on 41 lines in 25 files and `allowUnsafeReducibility` on 40 lines in 29 files.

Comparator's configuration names the five theorems below and permits the axioms `propext`, `Quot.sound` and `Classical.choice`.

## Claimed theorems

The five theorems Comparator's configuration names, in [src/Main.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/2d0c622a3464ba41ad98fca9086bab54fb74e303/src/Main.lean).

- [riemannHypothesis](riemannhypothesis.md)
- [riemannZeta_eq_zero_re](riemannzeta-eq-zero-re.md)
- [LFunction_ne_zero_of_half_lt_re](lfunction-ne-zero-of-half-lt-re.md)
- [LFunction_eq_zero_re](lfunction-eq-zero-re.md)
- [LFunction_eq_zero_re_of_isPrimitive](lfunction-eq-zero-re-of-isprimitive.md)

## Folders

A page per top-level folder of `src/`, and a part per second-level folder of 300 files or more.

- [Main and Statements](main-and-statements/README.md)
- [CompanionTheory](companiontheory/README.md)
- [Development](development/README.md)
- [Formalism](formalism/README.md)
- [GroundTheory](groundtheory/README.md)
- [Lemmata](lemmata/README.md)
- [PositivityTheory](positivitytheory/README.md)
- [ReciprocityTheory](reciprocitytheory/README.md)
