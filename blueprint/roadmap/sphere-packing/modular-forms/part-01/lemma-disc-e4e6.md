---
declaration: lemma
origin: cited
lean: ModularForm.discriminant_eq_E₄_cube_sub_E₆_sq
statement: formalized
proof: formalized
---

# disc-E4E6

We have

$$
\Delta(z) = (E_4^3-E_6^2)/1728.
$$

## Depends on

- [disc-definition](def-disc-definition.md)

## Proof

We only need to show its a cuspform, since once we have this, dividing the rhs by $\Delta$ would give a modular form of weight $0$ which is a constant, and so we can determine the constant easily.

To check its a cuspform, we just look at the $q$-expansions of $E_4$ and $E_6$ and prove directly that the first term vanishes.

## Lean

Formalized as [`ModularForm.discriminant_eq_E₄_cube_sub_E₆_sq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularForm.discriminant_eq_E₄_cube_sub_E₆_sq).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 239](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L239)
