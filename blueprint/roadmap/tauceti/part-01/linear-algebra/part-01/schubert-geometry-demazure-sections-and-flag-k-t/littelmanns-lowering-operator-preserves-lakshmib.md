---
declaration: theorem
origin: cited
lean: TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some
statement: formalized
proof: formalized
---

# Littelmann's lowering operator preserves Lakshmibai–Seshadri paths

Let `π` be an LS path of
dominant shape `λ`, realized in `V` by `f`, let `αᵢ` be a simple root and let `F` be a form on `V`
inducing the simple coroot pairing `⟨-, αᵢ^∨⟩`. If the lowering operator `f_αᵢ` is defined on the
path of `π`, then its result is again the path of an LS path of shape `λ`.

```lean
TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some.{u_1, u_2, u_3, u_4, u_5} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [AddCommGroup N] {P : RootPairing ι ℤ M N}
  {b : P.Base} [Finite ι] [P.IsReduced] {lam : M} {𝕜 : Type u_4} {V : Type u_5} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V]
  (π : TauCeti.LSPath P b lam) (hlam : lam ∈ P.dominantChamber b) (f : M →+ V) (i : ↥b.support)
  (F : Module.Dual 𝕜 V) (hF : ∀ (m : M), F (f m) = ↑((P.coroot' ↑i) m)) {q : TauCeti.PLPath 𝕜 V}
  (hq : TauCeti.PLPath.lower F (f (P.root ↑i)) (TauCeti.LSPath.toPLPath 𝕜 f π) = some q) :
  ∃ π', TauCeti.LSPath.toPLPath 𝕜 f π' = q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deodhar's lemma](../../../group-theory/coxeter/deodhars-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Lower.html#TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some).

## Sources

- [Tau Ceti documentation: `TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Lower.html#TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some)
- [Source of `TauCeti.LSPath.exists_toPLPath_eq_of_lower_eq_some` in TauCeti/RepresentationTheory/LSPath/Lower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/LSPath/Lower.lean#L423)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
