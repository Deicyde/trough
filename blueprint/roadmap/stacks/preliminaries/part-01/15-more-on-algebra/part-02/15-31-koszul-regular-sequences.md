---
declaration: section
origin: cited
lean: Koszul.IsKoszulRegularOn, Koszul.IsH1RegularOn, Koszul.IsKoszulRegular, Koszul.IsH1Regular, Koszul.isKoszulRegularOn_and_isKoszulRegular_of_regular, Koszul.IsKoszulRegularOn.isH1RegularOn, Koszul.IsKoszulRegular.isH1Regular, Koszul.isH1RegularOn_and_isKoszulRegularOn_snoc_mul
statement: formalized
proof: formalized
---

# 15.31 Koszul regular sequences

Section 15.31 of the Stacks Project, [Tag 062D](https://stacks.math.columbia.edu/tag/062D). 17 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 062E, a definition

[Tag 062E](https://stacks.math.columbia.edu/tag/062E) in the Stacks Project.

**`Koszul.IsKoszulRegularOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Defs.lean#L226). The attribute's comment: “(1)”.

> A sequence `f₁, …, f_r` is `M`-Koszul-regular if `Hᵢ(K_•(f) ⊗_R M) = 0` for all
> `i ≠ 0`.

```lean
def IsKoszulRegularOn (f : Fin r → R) (M : Type w) [AddCommGroup M] [Module R M] : Prop
```

**`Koszul.IsH1RegularOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Defs.lean#L231). The attribute's comment: “(2)”.

> A sequence `f₁, …, f_r` is `M`-`H₁`-regular if `H₁(K_•(f) ⊗_R M) = 0`.

```lean
def IsH1RegularOn (f : Fin r → R) (M : Type w) [AddCommGroup M] [Module R M] : Prop
```

**`Koszul.IsKoszulRegular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Defs.lean#L236). The attribute's comment: “(3)”.

> A sequence `f₁, …, f_r` is Koszul-regular if `Hᵢ(K_•(f)) = 0` for all `i ≠ 0`.

```lean
def IsKoszulRegular (f : Fin r → R) : Prop
```

**`Koszul.IsH1Regular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Defs.lean#L241). The attribute's comment: “(4)”.

> A sequence `f₁, …, f_r` is `H₁`-regular if `H₁(K_•(f)) = 0`.

```lean
def IsH1Regular (f : Fin r → R) : Prop
```

## Tag 062F, a lemma

[Tag 062F](https://stacks.math.columbia.edu/tag/062F) in the Stacks Project.

**`Koszul.isKoszulRegularOn_and_isKoszulRegular_of_regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 846](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L846).

> If every term of a finite sequence acts injectively on the quotient of `M` by its predecessors,
> then the sequence is `M`-Koszul-regular. In particular, an `M`-regular sequence is
> `M`-Koszul-regular, and a regular sequence in `R` is Koszul-regular.

```lean
theorem isKoszulRegularOn_and_isKoszulRegular_of_regular
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    {r : ℕ} {f : Fin r → R} :
    (RingTheory.Sequence.IsWeaklyRegular M (List.ofFn f) →
        Koszul.IsKoszulRegularOn f M) ∧
      (RingTheory.Sequence.IsRegular M (List.ofFn f) →
        Koszul.IsKoszulRegularOn f M) ∧
      (RingTheory.Sequence.IsRegular R (List.ofFn f) →
        Koszul.IsKoszulRegular f)
```

## Tag 0CEM, a lemma

[Tag 0CEM](https://stacks.math.columbia.edu/tag/0CEM) in the Stacks Project.

**`Koszul.IsKoszulRegularOn.isH1RegularOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L336). The attribute's comment: “(1)”.

> If the sequence `f_1, ..., f_r` is `M`-Koszul-regular, then it is `M`-H\_1-regular.

```lean
theorem IsKoszulRegularOn.isH1RegularOn {f : Fin r → R} {M : Type v} [AddCommGroup M]
    [Module R M] (h : IsKoszulRegularOn f M) : IsH1RegularOn f M
```

**`Koszul.IsKoszulRegular.isH1Regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L342). The attribute's comment: “(2)”.

> If the sequence `f_1, ..., f_r` is Koszul-regular, then it is H\_1-regular.

```lean
theorem IsKoszulRegular.isH1Regular {f : Fin r → R} (h : IsKoszulRegular f) : IsH1Regular f
```

## Tag 062G, a lemma

[Tag 062G](https://stacks.math.columbia.edu/tag/062G) in the Stacks Project.

**`Koszul.isH1RegularOn_and_isKoszulRegularOn_snoc_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L1073).

> Adjoining a product to a finite sequence preserves both `M`-`H₁`-regularity and
> `M`-Koszul-regularity when adjoining each factor separately has the corresponding property.

```lean
theorem isH1RegularOn_and_isKoszulRegularOn_snoc_mul
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    {n : ℕ} (s : Fin n → R) (f g : R) :
    ((Koszul.IsH1RegularOn (Fin.snoc s f) M ∧
        Koszul.IsH1RegularOn (Fin.snoc s g) M) →
      Koszul.IsH1RegularOn (Fin.snoc s (f * g)) M) ∧
    ((Koszul.IsKoszulRegularOn (Fin.snoc s f) M ∧
        Koszul.IsKoszulRegularOn (Fin.snoc s g) M) →
      Koszul.IsKoszulRegularOn (Fin.snoc s (f * g)) M)
```

## Tag 062H, a lemma

[Tag 062H](https://stacks.math.columbia.edu/tag/062H) in the Stacks Project.

**`KoszulC.isH1Regular_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/FlatBaseChange.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/FlatBaseChange.lean#L597). The attribute's comment: “(1)”.

> For a flat ring map `φ : R → S`, if `f_1, ..., f_r` is `M`-`H_1`-regular over `R`, then
> `φ(f_1), ..., φ(f_r)` is `(S ⊗_R M)`-`H_1`-regular over `S`.

```lean
theorem isH1Regular_baseChange {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Module.Flat R S] {r : ℕ} (f : Fin r → R) (M : Type*) [AddCommGroup M] [Module R M]
    (hf : IsH1RegularOn f M) :
    IsH1RegularOn (R := S) (fun i => algebraMap R S (f i)) (S ⊗[R] M)
```

**`KoszulC.isKoszulRegular_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/FlatBaseChange.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/FlatBaseChange.lean#L606). The attribute's comment: “(2)”. References: SGA 6 VII (1.5), “special case”; SGA 6 VIII (1.3), “VII 1.5, special case”.

> For a flat ring map `φ : R → S`, if `f_1, ..., f_r` is `M`-Koszul-regular over `R`, then
> `φ(f_1), ..., φ(f_r)` is `(S ⊗_R M)`-Koszul-regular over `S`.

```lean
theorem isKoszulRegular_baseChange {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Module.Flat R S] {r : ℕ} (f : Fin r → R) (M : Type*) [AddCommGroup M] [Module R M]
    (hf : IsKoszulRegularOn f M) :
    IsKoszulRegularOn (R := S) (fun i => algebraMap R S (f i)) (S ⊗[R] M)
```

## Tag 062I, a lemma

[Tag 062I](https://stacks.math.columbia.edu/tag/062I) in the Stacks Project.

**`Koszul.isQuasiRegular_of_isH1RegularOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Quasiregular.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Quasiregular.lean#L346).

> **Stacks 062I.** An `M`-`H₁`-regular sequence is `M`-quasi-regular.

```lean
public theorem isQuasiRegular_of_isH1RegularOn
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    {r : ℕ} {f : Fin r → R} (hf : Koszul.IsH1RegularOn f M) :
    RingTheory.Sequence.IsQuasiRegular M (List.ofFn f)
```

## Tag 09CC, a lemma

[Tag 09CC](https://stacks.math.columbia.edu/tag/09CC) in the Stacks Project.

**`Koszul.regular_koszulRegular_h1Regular_quasiRegular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Quasiregular.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Quasiregular.lean#L374). References: EGA 0 (15.1.11), “(1) ⇔ (4), local case”; EGA IV (19.5.1), “a)–c), local case”; EGA 0 (15.2.2), “converse: q-reg ⇒ reg”; EGA 0 (15.1.10), “special case”; EGA 0 (15.1.9), “special case”; EGA IV (16.9.12), “parenthetical”.

> **Stacks 09CC.** Let `M` be a nonzero finite module over a local Noetherian ring `R`, and
> let `f` be a finite sequence in the maximal ideal. Being `M`-regular, `M`-Koszul-regular,
> `M`-`H₁`-regular, and `M`-quasi-regular are equivalent. In particular, the corresponding
> four notions for the sequence in `R` are equivalent.

```lean
public theorem regular_koszulRegular_h1Regular_quasiRegular_tfae
    {R : Type u} [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Nontrivial M] [Module.Finite R M]
    {r : ℕ} (f : Fin r → R) (hf : ∀ i, f i ∈ IsLocalRing.maximalIdeal R) :
    List.TFAE
        [RingTheory.Sequence.IsRegular M (List.ofFn f),
          Koszul.IsKoszulRegularOn f M,
          Koszul.IsH1RegularOn f M,
          RingTheory.Sequence.IsQuasiRegular M (List.ofFn f)] ∧
      List.TFAE
        [RingTheory.Sequence.IsRegular R (List.ofFn f),
          Koszul.IsKoszulRegular f,
          Koszul.IsH1Regular f,
          RingTheory.Sequence.IsQuasiRegular R (List.ofFn f)]
```

## Tag 0665, a lemma

[Tag 0665](https://stacks.math.columbia.edu/tag/0665) in the Stacks Project.

**`Koszul.inf_span_eq_smul_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L351).

> Let `A` be a commutative ring, `I` an ideal of `A`, and `g_1, ..., g_m` elements of `A`. If the
> images of `g_1, ..., g_m` in `A/I` form an `H_1`-regular sequence, then
> `I ⊓ (g_1, ..., g_m) = I (g_1, ..., g_m)` as ideals of `A`.

```lean
theorem inf_span_eq_smul_span (I : Ideal A) (g : Fin m → A)
    (hreg : Koszul.IsH1Regular (fun i => Ideal.Quotient.mk I (g i))) :
    I ⊓ Ideal.span (Set.range g) = I * Ideal.span (Set.range g)
```

## Tag 0666, a lemma

[Tag 0666](https://stacks.math.columbia.edu/tag/0666) in the Stacks Project.

**`Koszul.inf_sq_eq_mul_of_quotient_generated_by_isH1Regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L451).

> If `I ⊆ J` and `J / I` is generated by an H₁-regular sequence, then `I ∩ J² = I J`.

```lean
theorem inf_sq_eq_mul_of_quotient_generated_by_isH1Regular
    {A : Type*} [CommRing A] (I J : Ideal A) (hIJ : I ≤ J)
    {m : ℕ} (g : Fin m → A ⧸ I)
    (hspan : Ideal.span (Set.range g) = Ideal.map (Ideal.Quotient.mk I) J)
    (hreg : Koszul.IsH1Regular g) :
    I ⊓ J ^ 2 = I * J
```

## Tag 0667, a lemma

[Tag 0667](https://stacks.math.columbia.edu/tag/0667) in the Stacks Project.

**`Koszul.isQuasiRegular_append_of_isH1Regular_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Concatenation/QuasiRegularAppend.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Concatenation/QuasiRegularAppend.lean#L567).

> **Stacks 0667.** If `f` is quasi-regular and the image of `g` modulo the ideal generated
> by `f` is H₁-regular, then the concatenation of `f` and `g` is quasi-regular.

```lean
public theorem isQuasiRegular_append_of_isH1Regular_quotient
    {A : Type*} [CommRing A] {n m : ℕ} (f : Fin n → A) (g : Fin m → A)
    (hf : RingTheory.Sequence.IsQuasiRegular A (List.ofFn f))
    (hg : Koszul.IsH1Regular
      (fun j => Ideal.Quotient.mk (Ideal.span (Set.range f)) (g j))) :
    RingTheory.Sequence.IsQuasiRegular A (List.ofFn (Fin.append f g))
```

## Tag 0668, a lemma

[Tag 0668](https://stacks.math.columbia.edu/tag/0668) in the Stacks Project.

**`Koszul.isH1Regular_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L289).

> Let `A` be a commutative ring, let `f : Fin n → A` be an `H_1`-regular sequence, let
> `I = (f_0, ..., f_{n-1})` be the ideal it generates, and let `g : Fin m → A` be such that the
> images `(Ideal.Quotient.mk I) ∘ g` form an `H_1`-regular sequence in `A/I`. Then the concatenated
> sequence `Fin.append f g : Fin (n + m) → A` is `H_1`-regular in `A`.

```lean
theorem isH1Regular_append {A : Type*} [CommRing A] {n m : ℕ}
    (f : Fin n → A) (g : Fin m → A)
    (hf : Koszul.IsH1Regular f)
    (hg : Koszul.IsH1Regular
      (fun j => (Ideal.Quotient.mk (Ideal.span (Set.range f))) (g j))) :
    Koszul.IsH1Regular (Fin.append f g)
```

## Tag 068L, a lemma

[Tag 068L](https://stacks.math.columbia.edu/tag/068L) in the Stacks Project.

**`Koszul.isH1Regular_quotient_of_isH1Regular_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Regular.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Regular.lean#L421).

> If `f_1, ..., f_n, g_1, ..., g_m` is an `H₁`-regular sequence in `A`, then the images
> `ḡ_1, ..., ḡ_m` of the `g_j` in the quotient `A / (f_1, ..., f_n)` form an `H₁`-regular sequence.

```lean
theorem isH1Regular_quotient_of_isH1Regular_append {A : Type*} [CommRing A] {n m : ℕ}
    (f : Fin n → A) (g : Fin m → A)
    (h : Koszul.IsH1Regular (Fin.append f g)) :
    Koszul.IsH1Regular
      (fun j : Fin m => Ideal.Quotient.mk (Ideal.span (Set.range f)) (g j))
```

## Tag 0669, a lemma

[Tag 0669](https://stacks.math.columbia.edu/tag/0669) in the Stacks Project.

**`Koszul.koszul_regular_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Concatenation/KoszulRegularAppend.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Concatenation/KoszulRegularAppend.lean#L706).

> If `f` is Koszul-regular and the image of `g` modulo the ideal generated by `f` is
> Koszul-regular, then the concatenation of `f` and `g` is Koszul-regular.

```lean
public theorem koszul_regular_append {A : Type*} [CommRing A] {n m : ℕ}
    (f : Fin n → A) (g : Fin m → A)
    (hf : Koszul.IsKoszulRegular f)
    (hg : Koszul.IsKoszulRegular
      (fun j => Ideal.Quotient.mk (Ideal.span (Set.range f)) (g j))) :
    Koszul.IsKoszulRegular (Fin.append f g)
```

## Tag 068M, a lemma

[Tag 068M](https://stacks.math.columbia.edu/tag/068M) in the Stacks Project.

**`Koszul.koszulRegular_quotient_of_koszulRegular_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Concatenation/KoszulRegularQuotient.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Concatenation/KoszulRegularQuotient.lean#L172).

> If `f` and the concatenation of `f` and `g` are Koszul-regular, then the image
> of `g` in the quotient by the ideal generated by `f` is Koszul-regular.

```lean
public theorem koszulRegular_quotient_of_koszulRegular_append
    {A : Type*} [CommRing A] {n m : ℕ} (f : Fin n → A) (g : Fin m → A)
    (hf : Koszul.IsKoszulRegular f)
    (hfg : Koszul.IsKoszulRegular (Fin.append f g)) :
    Koszul.IsKoszulRegular
      (fun j : Fin m => Ideal.Quotient.mk (Ideal.span (Set.range f)) (g j))
```

## Tag 066A, a lemma

[Tag 066A](https://stacks.math.columbia.edu/tag/066A) in the Stacks Project.

**`Koszul.regularity_of_generators_of_eq_span_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Concatenation/GeneratorIndependence.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Concatenation/GeneratorIndependence.lean#L434).

> **Stacks 066A.** If an ideal generated by `r` elements admits a quasi-regular,
> `H₁`-regular, or Koszul-regular generating sequence of length `r`, then every generating
> sequence of length `r` has the corresponding property.

```lean
public theorem regularity_of_generators_of_eq_span_range
    {R : Type*} [CommRing R] {r : ℕ} (I : Ideal R) (f : Fin r → R)
    (hf : Ideal.span (Set.range f) = I) :
    ((∃ g : Fin r → R, Ideal.span (Set.range g) = I ∧
        RingTheory.Sequence.IsQuasiRegular R (List.ofFn g)) →
      RingTheory.Sequence.IsQuasiRegular R (List.ofFn f)) ∧
    ((∃ g : Fin r → R, Ideal.span (Set.range g) = I ∧ Koszul.IsH1Regular g) →
      Koszul.IsH1Regular f) ∧
    ((∃ g : Fin r → R, Ideal.span (Set.range g) = I ∧ Koszul.IsKoszulRegular g) →
      Koszul.IsKoszulRegular f)
```

## Tag 068P, a lemma

[Tag 068P](https://stacks.math.columbia.edu/tag/068P) in the Stacks Project.

**`Stacks.GenericLinearForm.linearForm_isNonZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPolynomial/GenericLinearForm.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MvPolynomial/GenericLinearForm.lean#L149).

> **Stacks 068P**.
> If the only `x ∈ R` with `x a_i = 0` for all `i` is `x = 0`, then `f = ∑ a_i t_i` is a
> nonzerodivisor in `R[t_1, ..., t_n]`: every `g` with `f * g = 0` is zero.

```lean
theorem linearForm_isNonZeroDivisor (a : Fin n → R)
    (hinj : ∀ x : R, (∀ i, x * a i = 0) → x = 0) :
    ∀ g : MvPolynomial (Fin n) R, linearForm a * g = 0 → g = 0
```

## Tag 068Q, a lemma

[Tag 068Q](https://stacks.math.columbia.edu/tag/068Q) in the Stacks Project.

**`Koszul.isRegular_upperTriangular_of_isKoszulRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Descent.lean, line 1466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/Descent.lean#L1466).

> **Stacks 068Q.** A Koszul-regular sequence generating a proper ideal becomes a regular
> sequence after a generic invertible upper-triangular change of generators. The resulting
> polynomial localization is faithfully flat and smooth over the original ring, and the changed
> sequence generates the extension of the original ideal.

```lean
public theorem isRegular_upperTriangular_of_isKoszulRegular
    {R : Type*} [CommRing R] {n : ℕ} (f : Fin n → R)
    (hf : Koszul.IsKoszulRegular f)
    (hproper : Ideal.span (Set.range f) ≠ ⊤) :
    let σ := {ij : Fin n × Fin n // ij.1 ≤ ij.2}
    let P := MvPolynomial σ R
    let d : P := ∏ i : Fin n, MvPolynomial.X ⟨(i, i), le_rfl⟩
    let S := Localization.Away d
    let g : Fin n → S := fun i ↦
      ∑ j : Fin n, if hij : i ≤ j then
        algebraMap P S (MvPolynomial.X ⟨(i, j), hij⟩) * algebraMap R S (f j)
      else 0
    Module.FaithfullyFlat R S ∧ Algebra.Smooth R S ∧
      RingTheory.Sequence.IsRegular S (List.ofFn g) ∧
        Ideal.map (algebraMap R S) (Ideal.span (Set.range f)) =
          Ideal.span (Set.range g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.31, Tag 062D](https://stacks.math.columbia.edu/tag/062D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
