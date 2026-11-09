# Appendix A.3: The structure of proofs

> Some examples of proofs

*Quoted from [Analysis/Appendix_A_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 8 declarations: 8 proved here.

## Proposition A.3.1

An `example` ([line 11](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L11)). Proved here.

> Proposition A.3.1

```lean
example {A B C D: Prop} (hAC: A → C) (hCD: C → D) (hDB: D → B): A → B
```

An `example` ([line 31](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L31)). Proved here.

> Proposition A.3.1, alternate proof

```lean
example {A B C D: Prop} (hAC: A → C) (hCD: C → D) (hDB: D → B): A → B
```

An `example` ([line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L82)). Proved here.

> Proposition A.3.1, third proof

```lean
example {A B C D: Prop} (hAC: A → C) (hCD: C → D) (hDB: D → B): A → B
```

## Proposition A.3.2

An `example` ([line 19](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L19)). Proved here.

> Proposition A.3.2

```lean
example {x:ℝ} : x = Real.pi → Real.sin (x/2) + 1 = 2
```

An `example` ([line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L40)). Proved here.

> Proposition A.3.2, alternate proof

```lean
example {x:ℝ} : x = Real.pi → Real.sin (x/2) + 1 = 2
```

## Proposition A.3.3

An `example` ([line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L50)). Proved here.

> Proposition A.3.3

```lean
example {r:ℝ} (h: 0 < r) (h': r < 1) : Summable (fun n:ℕ ↦ n * r^n)
```

## Proposition A.3.4

An `example` ([line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L90)). Proved here.

> Proposition A.3.4

```lean
example {A B C D E F G H I:Prop} (hAE: A → E) (hEB: E ∧ B → F) (hADG : A → G → D) (hHI: H ∨ I) (hFHC : F ∧ H → C) (hAHG : A ∧ H → G) (hIG: I → G) (hIGC: G → C) : A ∧ B → C ∧ D
```

## Proposition A.3.5

An `example` ([line 107](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean#L107)). Proved here.

> Proposition A.3.5

```lean
example {A B C D:Prop} (hBC: B → C) (hAD: A → D) (hCD: D → ¬ C) : A → ¬ B
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_A_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_A_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_A_3.html)
