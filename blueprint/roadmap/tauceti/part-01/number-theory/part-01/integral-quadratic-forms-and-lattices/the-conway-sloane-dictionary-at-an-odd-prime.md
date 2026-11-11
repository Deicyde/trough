---
declaration: theorem
origin: cited
lean: TauCeti.conwaySloanePMass_mul_localDensity_toMatrix
statement: formalized
proof: formalized
---

# The Conway–Sloane dictionary at an odd prime

Let `B` be a bilinear form over `ℤ_p`, `p`
odd, with an orthogonal basis `b₀` whose diagonal entries are `B (b₀ i) (b₀ i) = uᵢ pᵏⁱ`. Then the
Gram matrix `A` of `B` in every basis `b`, with any index type, satisfies
`m_p · α_p(A) = p^{(n + 1) v_p(det A) / 2}`, where `m_p` is the Conway–Sloane `p`-mass of the
Jordan data `(uᵢ, kᵢ)` and `n` is the rank.

```lean
TauCeti.conwaySloanePMass_mul_localDensity_toMatrix.{u_1, u_2, u_3} {p : ℕ} [Fact (Nat.Prime p)]
  {M : Type u_1} [AddCommGroup M] [_root_.Module ℤ_[p] M] (hp : p ≠ 2) {ι : Type u_2} [Fintype ι]
  {B : LinearMap.BilinForm ℤ_[p] M} {b₀ : Module.Basis ι ℤ_[p] M} (hb₀ : B.iIsOrtho ⇑b₀)
  {u : ι → ℤ_[p]ˣ} {k : ι → ℕ} (hu : ∀ (i : ι), (B (b₀ i)) (b₀ i) = ↑(u i) * ↑p ^ k i)
  {κ : Type u_3} [Fintype κ] [DecidableEq κ] (b : Module.Basis κ ℤ_[p] M) :
  TauCeti.conwaySloanePMass p u k * ↑((LinearMap.BilinForm.toMatrix b) B).localDensity =
    √↑p ^ ((Fintype.card κ + 1) * ((LinearMap.BilinForm.toMatrix b) B).det.valuation)
```

## Depends on

- [The local density `α_p(A)` of a Gram matrix `A` over `ℤ_p`](the-local-density-p-a-of-a-gram-matrix-a-over-z.md)

## Proof depends on

- [The Conway–Sloane exponent identity](../../../algebra/part-02/other-results/the-conway-sloane-exponent-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.conwaySloanePMass_mul_localDensity_toMatrix`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LocalDensity/ConwaySloane.html#TauCeti.conwaySloanePMass_mul_localDensity_toMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.conwaySloanePMass_mul_localDensity_toMatrix`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LocalDensity/ConwaySloane.html#TauCeti.conwaySloanePMass_mul_localDensity_toMatrix)
- [Source of `TauCeti.conwaySloanePMass_mul_localDensity_toMatrix` in TauCeti/NumberTheory/IntegralLattice/LocalDensity/ConwaySloane.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/LocalDensity/ConwaySloane.lean#L233)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
