---
declaration: theorem
origin: cited
lean: theorem_A_2_4
statement: formalized
proof: formalized
---

# Appendix A.2: Implication

> An introduction to implications.  Showcases some basic tactics and Lean syntax.

*Quoted from [Analysis/Appendix_A_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 4 labelled items, carried by 4 declarations: 4 proved here. It also has 4 declarations and 21 examples with no label, counted here but not shown.

## Proposition A.2.2

An `example` ([line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean#L65)). Proved here.

> Proposition A.2.2

```lean
example : ((2+2:ℤ)=5) → (4=(10-4:ℤ))
```

## Theorem A.2.4

`theorem_A_2_4` (theorem, [line 73](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean#L73)). Proved here.

> Theorem A.2.4

```lean
theorem theorem_A_2_4 (n:ℤ) : Even (n * (n+1))
```

## Corollary A.2.5

An `example` ([line 81](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean#L81)). Proved here.

> Corollary A.2.5

```lean
example :
  let n:ℤ := (253+142)*123-(423+198)^342+538-213
  Even (n * (n+1))
```

## Proposition A.2.6

An `example` ([line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean#L129)). Proved here.

> Proposition A.2.6

```lean
example {x:ℝ} (h:x>0) (hsin: Real.sin x = 1) : x ≥ Real.pi / 2
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_A_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_A_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_A_2.html)
