---
declaration: theorem
origin: cited
lean: TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le, TauCeti.IsStronglyPseudoconvexAt.morseIndex_le
statement: formalized
proof: formalized
---

# The Morse index bound `λ ≤ n`

The real Hessian of a strictly plurisubharmonic function
has negative index of inertia at most the complex dimension.

```lean
TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℂ V] {f : V → ℝ} {x : V} [FiniteDimensional ℂ V]
  (h : TauCeti.IsStrictlyPlurisubharmonicAt f x) : TauCeti.morseIndex f x ≤ Module.finrank ℂ V
```

## Depends on

- [TauCeti.leviForm](../../../part-01/complex-morse-theory-affine-topology-and-weak-le/tauceti-leviform.md)

## Proof depends on

- [QuadraticForm.isTotallyReal_of_add_comp_posDef](../../../part-01/complex-morse-theory-affine-topology-and-weak-le/quadraticform-istotallyreal-of-add-comp-posdef.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pseudoconvex.html#TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le).

## Other forms

**The Morse index bound `λ ≤ n + q`.** Formalized in Tau Ceti as [`TauCeti.IsStronglyPseudoconvexAt.morseIndex_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pseudoconvex.html#TauCeti.IsStronglyPseudoconvexAt.morseIndex_le).

```lean
TauCeti.IsStronglyPseudoconvexAt.morseIndex_le.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℂ V] {f : V → ℝ} {x : V} {q : ℕ} [FiniteDimensional ℂ V]
  (h : TauCeti.IsStronglyPseudoconvexAt q f x) : TauCeti.morseIndex f x ≤ Module.finrank ℂ V + q
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pseudoconvex.html#TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le)
- [Source of `TauCeti.IsStrictlyPlurisubharmonicAt.morseIndex_le` in TauCeti/Analysis/Complex/Pseudoconvex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Pseudoconvex.lean#L171)
