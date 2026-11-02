---
declaration: theorem
origin: cited
lean: Completeness
statement: formalized
proof: formalized
---

# Birkhoff's completeness theorem

For any theory $\Gamma$ and words $w, w'$ over a fixed alphabet

$$
\Gamma\vdash w\simeq w'\ \mathrm{iff}\ \Gamma\models w\simeq w'.
$$

## Depends on

- [Models](models-def.md)
- [Derivation](derivation-def.md)

## Proof

(Sketch) The ‘only if’ component is soundness, and follows from verifying that the rules of inference in [Derivation](derivation-def.md) holds for $\models$. The ‘if’ part is completeness, and is proven by constructing the magma of words, quotiented out by the relation $\Gamma \vdash w \simeq w'$, which is easily seen to be an equivalence relation respecting the magma operation.

## Lean

Formalized as [`Completeness`](https://teorth.github.io/equational_theories/docs/find/#doc/Completeness).

## Sources

- [Equational Theories blueprint: chapter/intro.tex, line 109](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L109)
