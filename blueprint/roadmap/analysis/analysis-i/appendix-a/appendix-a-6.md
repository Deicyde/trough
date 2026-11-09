# Appendix A.6: Some examples of proofs and quantifiers

> Some examples of proofs and quantifiers in Lean

*Quoted from [Analysis/Appendix_A_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 2 labelled items, carried by 3 declarations: 3 proved here. It also has 1 example with no label, counted here but not shown.

## Proposition A.6.1

An `example` ([line 13](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_6.lean#L13)). Proved here.

> Proposition A.6.1

```lean
example : ∀ ε > (0:ℝ), ∃ δ > 0, 2 * δ < ε
```

## Proposition A.6.2

An `example` ([line 25](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_6.lean#L25)). Proved here.

> Proposition A.6.2.  The proof below is somewhat non-idiomatic for Lean, but illustrates how to implement a "let ε be a quantity to be chosen later" type of proof.

```lean
example : ∃ ε > 0, ∀ x, 0 < x ∧ x < ε → sin x > x / 2
```

An `example` ([line 56](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_6.lean#L56)). Proved here.

> Proposition A.6.2: a more idiomatic proof

```lean
example : ∃ ε > 0, ∀ x, 0 < x ∧ x < ε → sin x > x / 2
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_A_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_A_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_A_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_A_6.html)
