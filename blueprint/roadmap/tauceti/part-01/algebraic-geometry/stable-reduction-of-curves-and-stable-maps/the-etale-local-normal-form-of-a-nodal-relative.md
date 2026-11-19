---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing
statement: formalized
proof: formalized
---

# The étale local normal form of a nodal relative curve over a discrete valuation ring

Let
`S` be a standard syntomic algebra of relative dimension one over a discrete valuation ring `R`
with uniformizer `π`, whose singular locus `S ⧸ Fitt₁(Ω[S⁄R])` is unramified over `R`, and let `q`
be a prime of `S` in the singular locus lying over the closed point of `R`. Then there are

* a discrete valuation ring `R'` which is an étale `R`-algebra with local structure map, in which
  `π` remains a uniformizer,
* an étale `S`-algebra `T` which is an `R'`-algebra compatibly over `R`, with a prime `Q` lying
  over `q` and over the closed point of `R'`, and
* an étale `R'`-algebra map `φ : R'[u, v] ⧸ (uv - b) → T` sending both coordinates into `Q`,
  where `b = 0` or `b = πⁿ` for some `n > 0`.

```lean
TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing.{u}
  {R S : Type u} [CommRing R] [CommRing S] [Algebra R S] [Algebra.EssFiniteType R S]
  [Algebra.FormallyUnramified R (S ⧸ TauCeti.fittingIdeal S Ω[S⁄R] 1)]
  [TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension 1 R S] [IsDomain R]
  [IsDiscreteValuationRing R] {π : R} (hπ : Irreducible π) (q : Ideal S) [q.IsPrime]
  (hq : TauCeti.fittingIdeal S Ω[S⁄R] 1 ≤ q)
  (hqR : Ideal.comap (algebraMap R S) q = IsLocalRing.maximalIdeal R) :
  ∃ R' x,
    ∃ (x_1 : IsDomain R') (x_2 : IsDiscreteValuationRing R'),
      ∃ x_3,
        ∃ (_ : Algebra.Etale R R') (_ : IsLocalHom (algebraMap R R')),
          ∃ T x_6 x_7,
            ∃ (_ : Algebra.Etale S T),
              ∃ x_9 x_10,
                ∃ (_ : IsScalarTower R S T) (_ : IsScalarTower R R' T),
                  ∃ Q,
                    ∃ (_ : Q.IsPrime),
                      ∃ b φ,
                        Irreducible ((algebraMap R R') π) ∧
                          (b = 0 ∨ ∃ n, 0 < n ∧ b = (algebraMap R R') π ^ n) ∧
                            q = Ideal.comap (algebraMap S T) Q ∧
                              Ideal.comap (algebraMap R' T) Q = IsLocalRing.maximalIdeal R' ∧
                                φ (TauCeti.NodeAlgebra.coord b 0) ∈ Q ∧
                                  φ (TauCeti.NodeAlgebra.coord b 1) ∈ Q ∧ φ.Etale
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Node/LocalNormalForm.html#TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Node/LocalNormalForm.html#TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing)
- [Source of `TauCeti.Algebra.IsStandardSyntomicOfRelativeDimension.exists_etale_nodeAlgebra_hom_of_isDiscreteValuationRing` in TauCeti/RingTheory/Node/LocalNormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Node/LocalNormalForm.lean#L324)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
