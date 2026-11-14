---
declaration: lemma
origin: cited
lean: modular_slash_negI_of_even
statement: formalized
proof: formalized
---

# slash-negI-even-weight

For even $k$, $F|_{k}(-I) = F$.

## Depends on

- [slash-operator](def-slash-operator.md)

## Proof

Follows from the definition of the slash operator: $(F|_{k}(-I))(z) = (-1)^{-k}F((-I)z) = F(z)$.

## Lean

Formalized as [`modular_slash_negI_of_even`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/modular_slash_negI_of_even).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 80](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L80)
