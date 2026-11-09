# Appendix A.7: Equality

> Introduction to equality in Lean

*Quoted from [Analysis/Appendix_A_7.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_7.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 3 labelled items, carried by 3 declarations: 2 proved here and 1 stated without proof (1 of them exercises). It also has 5 declarations and 10 examples with no label, counted here but not shown.

## Example A.7.1

An `example` ([line 61](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_7.lean#L61)). Proved here.

> Example A.7.1

```lean
example {x y:ℝ} (h:x = y) : 2*x = 2*y ∧ sin x = sin y ∧ ∀ z, x + z = y + z
```

## Example A.7.2

An `example` ([line 69](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_7.lean#L69)). Proved here.

> Example A.7.2

```lean
example {n m:ℤ} (hn: Odd n) (h: n = m) : Odd m
```

## Exercise A.7.1

An `example` ([line 112](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_7.lean#L112)). An exercise, stated without proof.

> Exercise A.7.1

```lean
example {a b c d:ℝ} (hab: a = b) (hcd : c = d) : a + d = b + c
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_A_7.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_7.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_A_7/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_A_7.html)
