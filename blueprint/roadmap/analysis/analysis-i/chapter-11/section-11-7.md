---
declaration: theorem
origin: cited
lean: Chapter11.not_integrable
statement: formalized
proof: formalized
---

# Section 11.7: A non-Riemann integrable function

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - An example of a bounded function on a compact interval that is not Riemann integrable.

*Quoted from [Analysis/Section_11_7.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_7.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 1 labelled item, carried by 1 declaration: 1 proved here.

## Proposition 11.7.1

`Chapter11.not_integrable` (theorem, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_7.lean#L23)). Proved here.

> Proposition 11.7.1

```lean
theorem not_integrable : BddOn f_9_3_21 (Icc 0 1) ∧ ¬ IntegrableOn f_9_3_21 (Icc 0 1)
```

## Depends on

- [Section 11.4: Basic properties of the Riemann integral](section-11-4.md)

## Sources

- [Analysis/Section_11_7.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_7.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_7/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_7.html)
