---
declaration: section
origin: cited
lean: IsFormallySmooth, RingHom.FormallySmoothTop.of_formallySmooth_of_isAdic, isFormallySmooth_of_formallySmooth_and_isAdic_and_iff_discrete, RingHom.FormallySmoothNAdic, isFormallySmooth_iff_adicCompletion, RingHom.FormallySmoothTop.exists_continuous_lift_of_isAdic, exists_continuous_lift_of_isFormallySmooth_of_isAdic, RingHom.FormallySmoothNAdic.mono
statement: formalized
proof: formalized
---

# 15.38 Formally smooth maps of topological rings

Section 15.38 of the Stacks Project, [Tag 07EA](https://stacks.math.columbia.edu/tag/07EA). 9 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07EB, a definition

[Tag 07EB](https://stacks.math.columbia.edu/tag/07EB) in the Stacks Project.

**`IsFormallySmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicCriterion.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicCriterion.lean#L96). References: EGA 0 (19.3.1), “linearly topologized”.

> A homomorphism between linearly topologized rings is formally smooth if it
> is continuous and every compatible square-zero lifting problem with a discrete
> target ring has a continuous lift.

```lean
def IsFormallySmooth.{u, v, w} {R : Type v} {S : Type w}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R] [IsLinearTopology R R]
    [CommRing S] [TopologicalSpace S] [IsTopologicalRing S] [IsLinearTopology S S]
    (φ : R →+* S) : Prop
```

## Tag 07EC, a lemma

[Tag 07EC](https://stacks.math.columbia.edu/tag/07EC) in the Stacks Project.

**`RingHom.FormallySmoothTop.of_formallySmooth_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Algebraic.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Algebraic.lean#L25). References: EGA 0 (19.3.8), “discrete topologies”.

> Algebraic formal smoothness implies topological formal smoothness for an adic target.

```lean
theorem of_formallySmooth_of_isAdic.{u, v, w}
    {R : Type v} {S : Type w} [CommRing R] [CommRing S]
    [TopologicalSpace R] [IsTopologicalRing R]
    [TopologicalSpace S] [IsTopologicalRing S]
    (phi : R →+* S) (n : Ideal S) (hn : IsAdic n)
    (hphi : @Algebra.FormallySmooth R S _ _ phi.toAlgebra) :
    RingHom.FormallySmoothTop.{u, v, w} phi
```

**`isFormallySmooth_of_formallySmooth_and_isAdic_and_iff_discrete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicCriterion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicCriterion.lean#L181).

> Algebraic formal smoothness implies formal smoothness for any continuous
> map from a linearly topologized ring to a pre-adic ring. Moreover, for ideals
> `m ⊆ R` and `n ⊆ S`, a continuous map for the adic topologies is formally
> smooth if and only if it is formally smooth with the discrete topology on
> `R`.

```lean
public theorem isFormallySmooth_of_formallySmooth_and_isAdic_and_iff_discrete.{u, v, w}
    {R : Type v} {S : Type w} [CommRing R] [CommRing S] (φ : R →+* S) :
    (∀ (tR : TopologicalSpace R) (tS : TopologicalSpace S),
      letI := tR
      letI := tS
      ∀ [IsTopologicalRing R] [IsLinearTopology R R]
        [IsTopologicalRing S] [IsLinearTopology S S],
        (∃ n : Ideal S, IsAdic n) →
          @Algebra.FormallySmooth R S _ _ φ.toAlgebra → Continuous φ →
            IsFormallySmooth.{u} φ) ∧
      ∀ (m : Ideal R) (n : Ideal S),
        (letI := m.adicTopology
         letI : IsTopologicalRing R := m.ringFilterBasis.isTopologicalRing
         letI := n.adicTopology
         letI : IsTopologicalRing S := n.ringFilterBasis.isTopologicalRing
         @Continuous R S m.adicTopology n.adicTopology φ) →
          ((letI := m.adicTopology
            letI : IsTopologicalRing R := m.ringFilterBasis.isTopologicalRing
            letI : IsLinearTopology R R := m.isLinearTopology
            letI := n.adicTopology
            letI : IsTopologicalRing S := n.ringFilterBasis.isTopologicalRing
            letI : IsLinearTopology S S := n.isLinearTopology
            IsFormallySmooth.{u} φ) ↔
           (letI : TopologicalSpace R := ⊥
            letI : DiscreteTopology R := ⟨rfl⟩
            letI := n.adicTopology
            letI : IsTopologicalRing S := n.ringFilterBasis.isTopologicalRing
            letI : IsLinearTopology S S := n.isLinearTopology
            IsFormallySmooth.{u} φ))
```

## Tag 07NI, a definition

[Tag 07NI](https://stacks.math.columbia.edu/tag/07NI) in the Stacks Project.

**`RingHom.FormallySmoothNAdic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Topological.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Topological.lean#L144).

> `φ : R →+* S` is *formally smooth for the `n`-adic topology*, where `n` is an
> ideal of `S`: for every square-zero ideal `J` of a ring `A`, every ring map
> `f : R → A`, and every ring map `ψ : S → A ⧸ J` making the square commute and
> with `ψ` killing some power of `n` (some `k ≥ 1` with `n ^ k ≤ ker ψ`), there
> exists a lift `g : S → A` with
> `(Ideal.Quotient.mk J) ∘ g = ψ` and `g ∘ φ = f`.

```lean
def FormallySmoothNAdic {R : Type v} {S : Type w} [CommRing R] [CommRing S]
    (φ : R →+* S) (n : Ideal S) : Prop
```

## Tag 07ED, a lemma

[Tag 07ED](https://stacks.math.columbia.edu/tag/07ED) in the Stacks Project.

**`isFormallySmooth_iff_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/Completion.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/Completion.lean#L472). References: EGA 0 (19.3.6), “adic top., f.g. ideals”; EGA 0 (19.9.4), “a) <=> b) <=> c)”; EGA IV (17.5.3), “d) ⇔ d')”.

> Formal smoothness of a continuous homomorphism of adic rings is unchanged
> by completing the target, or by completing both source and target.
>
> The hypotheses are exactly those of Stacks 07ED: rings `R` and `S` with
> finitely generated ideals `m` and `n`, endowed with the `m`-adic and `n`-adic
> topologies, and a continuous ring homomorphism `f : R →+* S`. The completions
> carry the adic topologies of the extended ideals `m R^∧` and `n S^∧`; since `m`
> and `n` are finitely generated, these are the `m`-adic and `n`-adic topologies
> of the completions (Stacks 05GG).

```lean
public theorem isFormallySmooth_iff_adicCompletion.{u, v, w}
    {R : Type v} {S : Type w} [CommRing R] [CommRing S]
    (m : Ideal R) (n : Ideal S) (hm : m.FG) (hn : n.FG) (f : R →+* S)
    (hf : @Continuous R S m.adicTopology n.adicTopology f) :
    letI : WithIdeal R := ⟨m⟩
    letI : WithIdeal S := ⟨n⟩
    let mhat : Ideal (Completion R) := m.map Completion.coeRingHom
    let nhat : Ideal (Completion S) := n.map Completion.coeRingHom
    let fhat : Completion R →+* Completion S := Completion.mapRingHom f hf
    let toShat : R →+* Completion S := Completion.coeRingHom.comp f
    letI : TopologicalSpace (Completion R) := mhat.adicTopology
    letI : IsTopologicalRing (Completion R) := mhat.nonarchimedean.toIsTopologicalRing
    letI : IsLinearTopology (Completion R) (Completion R) := mhat.isLinearTopology
    letI : TopologicalSpace (Completion S) := nhat.adicTopology
    letI : IsTopologicalRing (Completion S) := nhat.nonarchimedean.toIsTopologicalRing
    letI : IsLinearTopology (Completion S) (Completion S) := nhat.isLinearTopology
    (IsFormallySmooth.{u} f ↔ IsFormallySmooth.{u} toShat) ∧
      (IsFormallySmooth.{u} toShat ↔ IsFormallySmooth.{u} fhat)
```

## Tag 07NJ, a lemma

[Tag 07NJ](https://stacks.math.columbia.edu/tag/07NJ) in the Stacks Project.

**`RingHom.FormallySmoothTop.exists_continuous_lift_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/AdicLifting.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/AdicLifting.lean#L508).

> A formally smooth homomorphism lifts continuously through a closed quotient of an adic
> complete ring, provided a positive power of the quotient ideal lies in an ideal of definition.

```lean
theorem exists_continuous_lift_of_isAdic
    {R : Type u} {S : Type v} {A : Type w}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R] [IsLinearTopology R R]
    [CommRing S] [TopologicalSpace S] [IsTopologicalRing S] [IsLinearTopology S S]
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    (f : R →+* S) (n : Ideal S) (hn : IsAdic n)
    (hf : RingHom.FormallySmoothTop.{w} f)
    (I : Ideal A) (hI : IsAdic I) [IsAdicComplete I A]
    (J : Ideal A) (hJ : IsClosed (J : Set A))
    (t : ℕ) (ht : 1 ≤ t) (hJI : J ^ t ≤ I)
    (g : R →+* A) (hg : Continuous g)
    (ψ : S →+* A ⧸ J) (hψ : Continuous ψ)
    (hcomm : ψ.comp f = (Ideal.Quotient.mk J).comp g) :
    ∃ φ : S →+* A, Continuous φ ∧ φ.comp f = g ∧
      (Ideal.Quotient.mk J).comp φ = ψ
```

**`exists_continuous_lift_of_isFormallySmooth_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicBaseChange.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicBaseChange.lean#L129).

> A formally smooth homomorphism for the `n`-adic topology lifts continuously through a closed
> quotient of an adic ring when a positive power of the quotient ideal lies in an ideal of
> definition.

```lean
public theorem exists_continuous_lift_of_isFormallySmooth_of_isAdic
    {R : Type u} {S : Type v} {A : Type w}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R] [IsLinearTopology R R]
    [CommRing S] [TopologicalSpace S] [IsTopologicalRing S] [IsLinearTopology S S]
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    (f : R →+* S) (n : Ideal S) (hn : IsAdic n)
    (hf : IsFormallySmooth.{w} f)
    (I : Ideal A) (hI : IsAdic I) [IsAdicComplete I A]
    (J : Ideal A) (hJ : IsClosed (J : Set A))
    (t : ℕ) (ht : 1 ≤ t) (hJI : J ^ t ≤ I)
    (g : R →+* A) (hg : Continuous g)
    (ψ : S →+* A ⧸ J) (hψ : Continuous ψ)
    (hcomm : ψ.comp f = (Ideal.Quotient.mk J).comp g) :
    ∃ φ : S →+* A, Continuous φ ∧ φ.comp f = g ∧
      (Ideal.Quotient.mk J).comp φ = ψ
```

## Tag 07EE, a lemma

[Tag 07EE](https://stacks.math.columbia.edu/tag/07EE) in the Stacks Project.

**`RingHom.FormallySmoothNAdic.mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Topological.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Topological.lean#L158). References: EGA 0 (19.3.8), “adic topologies on S”.

> Stacks Tag 07EE, Lemma 15.38.6: if `n ≤ n'` are ideals of `S` and `φ : R → S`
> is formally smooth for the `n`-adic topology, then it is formally smooth for the
> `n'`-adic topology. Usable as `h.mono hnn'`.

```lean
theorem FormallySmoothNAdic.mono {R : Type v} {S : Type w} [CommRing R] [CommRing S]
    {φ : R →+* S} {n n' : Ideal S} (h : FormallySmoothNAdic.{u, v, w} φ n) (hnn' : n ≤ n') :
    FormallySmoothNAdic.{u, v, w} φ n'
```

## Tag 07EF, a lemma

[Tag 07EF](https://stacks.math.columbia.edu/tag/07EF) in the Stacks Project.

**`RingHom.FormallySmoothTop.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Topological.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Topological.lean#L108).

> Stacks Lemma 15.38.7 (Tag 07EF). A composition of formally smooth continuous
> ring homomorphisms of topological rings is formally smooth: if `φ : R →+* S` and
> `ψ : S →+* T` are formally smooth and `ψ` is continuous, then `ψ.comp φ` is
> formally smooth. Usable as `hsφ.comp hsψ hψ`. Continuity of `ψ.comp φ` is not
> part of the conclusion; it follows from `Continuous.comp` given that `φ` is
> continuous.

```lean
theorem FormallySmoothTop.comp {R : Type v} {S : Type w} {T : Type z}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
    [CommRing S] [TopologicalSpace S] [IsTopologicalRing S]
    [CommRing T] [TopologicalSpace T] [IsTopologicalRing T] {φ : R →+* S} {ψ : S →+* T}
    (hsφ : FormallySmoothTop.{u, v, w} φ) (hsψ : FormallySmoothTop.{u, w, z} ψ)
    (hψ : Continuous ψ) : FormallySmoothTop.{u, v, z} (ψ.comp φ)
```

## Tag 07EG, a lemma

[Tag 07EG](https://stacks.math.columbia.edu/tag/07EG) in the Stacks Project.

**`RingHom.formallySmoothTop_iff_formallySmoothNAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Adic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Adic.lean#L69).

> For a discrete source and an adic target, topological formal smoothness is equivalent to
> formal smoothness for the adic topology.

```lean
theorem formallySmoothTop_iff_formallySmoothNAdic.{u, v, w}
    {R : Type v} {S : Type w} [CommRing R] [CommRing S]
    [TopologicalSpace R] [IsTopologicalRing R] [DiscreteTopology R]
    [TopologicalSpace S] [IsTopologicalRing S]
    (phi : R →+* S) (n : Ideal S) (hn : IsAdic n) :
    FormallySmoothTop.{u, v, w} phi ↔ FormallySmoothNAdic.{u, v, w} phi n
```

**`RingHom.FormallySmoothNAdic.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/BaseChange.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/BaseChange.lean#L32). References: EGA 0 (19.3.5), “(iii)”; EGA 0 (19.9.3), “adic topology case”.

> Formal smoothness for the `n`-adic topology is preserved by arbitrary base change from
> `R` to `R'`; on `S ⊗[R] R'`, the adic ideal is the extension of `n`.

```lean
theorem baseChange.{u, v, w, z}
    {R : Type v} {S : Type w} {R' : Type z}
    [CommRing R] [CommRing S] [CommRing R'] [Algebra R S] [Algebra R R']
    (n : Ideal S) (h : RingHom.FormallySmoothNAdic.{u, v, w} (algebraMap R S) n) :
    RingHom.FormallySmoothNAdic.{u, z, max w z}
      (Algebra.TensorProduct.includeRight (R := R) (A := S) (B := R')).toRingHom
      (n.map (Algebra.TensorProduct.includeLeft (R := R) (S := R)
        (A := S) (B := R')).toRingHom)
```

## Tag 07EH, a lemma

[Tag 07EH](https://stacks.math.columbia.edu/tag/07EH) in the Stacks Project.

**`isFormallySmooth_adic_of_split_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicBaseChange.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/TopologicalRings/AdicBaseChange.lean#L374).

> If `R → R'` admits an `R`-linear retraction and the base change
> `R' → S ⊗[R] R'` is formally smooth for the topology defined by the
> extension of `n`, then `R → S` is formally smooth for the `n`-adic topology.

```lean
public theorem isFormallySmooth_adic_of_split_baseChange.{u, v, w, z}
    {R : Type v} {S : Type w} {R' : Type z}
    [CommRing R] [CommRing S] [CommRing R'] [Algebra R S] [Algebra R R']
    (n : Ideal S)
    (hsplit : ∃ p : R' →ₗ[R] R,
      p.comp (Algebra.linearMap R R') = LinearMap.id)
    (hsmooth :
      letI : Algebra R' (S ⊗[R] R') :=
        Algebra.TensorProduct.rightAlgebra (R := R) (A := S) (B := R')
      let n' : Ideal (S ⊗[R] R') :=
        Ideal.map (Algebra.TensorProduct.includeLeft : S →ₐ[R] S ⊗[R] R') n
      letI : TopologicalSpace R' := ⊥
      letI : DiscreteTopology R' := ⟨rfl⟩
      letI : TopologicalSpace (S ⊗[R] R') := n'.adicTopology
      letI : IsTopologicalRing (S ⊗[R] R') := n'.ringFilterBasis.isTopologicalRing
      letI : IsLinearTopology (S ⊗[R] R') (S ⊗[R] R') := n'.isLinearTopology
      IsFormallySmooth.{max u z} (algebraMap R' (S ⊗[R] R'))) :
    letI : TopologicalSpace R := ⊥
    letI : DiscreteTopology R := ⟨rfl⟩
    letI : TopologicalSpace S := n.adicTopology
    letI : IsTopologicalRing S := n.ringFilterBasis.isTopologicalRing
    letI : IsLinearTopology S S := n.isLinearTopology
    IsFormallySmooth.{u} (algebraMap R S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.38, Tag 07EA](https://stacks.math.columbia.edu/tag/07EA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
