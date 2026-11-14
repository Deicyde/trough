---
declaration: theorem
origin: cited
lean: KummerCriterion.map_comap_eq_ringOfIntegers
statement: formalized
proof: formalized
---

# map-comap-ring-of-integers

If $J$ is an ideal of $\mathcal O_{L^+}$, then extension to $\mathcal O_L$ followed by contraction is the identity:

$$
(J\mathcal O_L)\cap\mathcal O_{L^+}=J.
$$

## Depends on

- [cm-real-subfield](../the-real-subfield-and-the-class-numbers/def-cm-real-subfield.md)

## Proof

For a faithfully flat ring map $A \to B$, every ideal $J \subseteq A$ satisfies $JB \cap A = J$: the inclusion $J \subseteq JB \cap A$ is clear, and the quotient map $A/J \to B/JB$ is injective by faithful flatness of $B/JB$ over $A/J$. It remains to note that $\mathcal O_L$ is faithfully flat over $\mathcal O_{L^+}$: it is a finitely generated torsion-free module over the Dedekind domain $\mathcal O_{L^+}$, hence projective, hence flat, and $\operatorname{Spec}\mathcal O_L \to \operatorname{Spec}\mathcal O_{L^+}$ is surjective because the integral extension $\mathcal O_{L^+} \subseteq \mathcal O_L$ satisfies lying-over.

## Lean

Formalized as [`KummerCriterion.map_comap_eq_ringOfIntegers`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.map_comap_eq_ringOfIntegers).

## Sources

- [Kummer's criterion blueprint: subsections/cm-splitting.tex, line 44](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cm-splitting.tex#L44)
