---
declaration: module
origin: cited
lean: Ket.normalize_ket_eq_self, Braket.dot_self_eq_one, Ket.IsProd_prod, Ket.not_IsEntangled_prod, Ket.IsProd_iff_mul_eq_mul, Ket.MES_isEntangled, transposeTrick, Ket
statement: formalized
proof: formalized
---

# QuantumInfo.States.Pure.Braket

The module `QuantumInfo.States.Pure.Braket`, [QuantumInfo/States/Pure/Braket.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean): 63 declarations, 40 with a docstring, 7 listed as significant; 3 private, not shown.

> Finite dimensional quantum pure states, bra and kets. Mixed states are `MState` in that file.
>
> These could be done with a Hilbert space of Fintype, which would look like
> ```lean4
> (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] [FiniteDimensional ℂ H]
> ```
> or by choosing a particular `Basis` and asserting it is `Fintype`. But frankly it seems easier to
> mostly focus on the basis-dependent notion of `Matrix`, which has the added benefit of an obvious
> "classical" interpretation (as the basis elements, or diagonal elements of a mixed state). In that
> sense, this quantum theory comes with the a particular classical theory always preferred.

**`Ket`**, a structure, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L40).

> A ket as a vector of unit norm. We follow the convention in `Matrix` of vectors as simple functions
> from a Fintype. Kets are distinctly not a vector space in our notion, as they represent only normalized
> states and so cannot (in general) be added or scaled.

```lean
structure Ket where
  vec : d → ℂ
  normalized' : ∑ x, ‖vec x‖ ^ 2 = 1
```

**`Bra`**, a structure, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L47).

> A bra is identical in definition to a `Ket`, but are separate to avoid complex conjugation confusion.
> They can be interconverted with the adjoint: `Ket.to_bra` and `Bra.to_ket`

```lean
structure Bra where
  vec : d → ℂ
  normalized' : ∑ x, ‖vec x‖ ^ 2 =1
```

**`Braket.instFunLikeKet`**, an instance, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L61).

```lean
instance instFunLikeKet : FunLike (Ket d) d ℂ
```

**`Ket.coe_fun_eq`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L65).

```lean
lemma _root_.Ket.coe_fun_eq (ψ : Ket d) : (ψ : d → ℂ) = ψ.vec
```

**`Braket.instFunLikeBra`**, an instance, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L67).

```lean
instance instFunLikeBra : FunLike (Bra d) d ℂ
```

**`Bra.coe_fun_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L71).

```lean
lemma _root_.Bra.coe_fun_eq (ψ : Bra d) : (ψ : d → ℂ) = ψ.vec
```

**`Braket.dot`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L73).

```lean
def dot (ξ : Bra d) (ψ : Ket d) : ℂ
```

**`Braket.dot_eq_dotProduct`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L77).

```lean
lemma dot_eq_dotProduct (ψ : Bra d) (φ : Ket d) :〈ψ‖φ〉= dotProduct (m := d) ψ φ
```

**`Ket.apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L87).

```lean
lemma Ket.apply (ψ : Ket d) (i : d) : ψ i = ψ.vec i
```

**`Bra.apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L90).

```lean
lemma Bra.apply (ψ : Bra d) (i : d) : ψ i = ψ.vec i
```

**`Ket.ext`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L94).

```lean
lemma Ket.ext {ξ ψ : Ket d} (h : ∀ x, ξ x = ψ x) : ξ = ψ
```

**`Bra.ext`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L98).

```lean
lemma Bra.ext {ξ ψ : Bra d} (h : ∀ x, ξ x = ψ x) : ξ = ψ
```

**`Ket.normalized`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L101).

```lean
lemma Ket.normalized (ψ : Ket d) : ∑ x, Complex.normSq (ψ x) = 1
```

**`Bra.normalized`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L106).

```lean
lemma Bra.normalized (ψ : Bra d) : ∑ x, Complex.normSq (ψ x) = 1
```

**`Ket.to_bra`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L113).

> Any Bra can be turned into a Ket by conjugating the elements.

```lean
def Ket.to_bra (ψ : Ket d) : Bra d
```

**`Bra.to_ket`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L118).

> Any Ket can be turned into a Bra by conjugating the elements.

```lean
def Bra.to_ket (ψ : Bra d) : Ket d
```

**`instBraOfKet`**, an instance, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L121).

```lean
instance instBraOfKet : Coe (Ket d) (Bra d)
```

**`instKetOfBra`**, an instance, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L123).

```lean
instance instKetOfBra : Coe (Bra d) (Ket d)
```

**`Bra.eq_conj`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L126).

```lean
lemma Bra.eq_conj (ψ : Ket d) (x : d) :〈ψ∣ x = conj (∣ψ〉 x)
```

**`Bra.apply'`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L129).

```lean
lemma Bra.apply' (ψ : Ket d) (i : d) : 〈ψ∣ i = conj (ψ.vec i)
```

**`Ket.exists_ne_zero`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L132).

```lean
lemma Ket.exists_ne_zero (ψ : Ket d) : ∃ x, ψ x ≠ 0
```

**`Bra.exists_ne_zero`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L139).

```lean
lemma Bra.exists_ne_zero (ψ : Bra d) : ∃ x, ψ x ≠ 0
```

**`Ket.normalize`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L147).

> Create a ket out of a vector given it has a nonzero component

```lean
def Ket.normalize (v : d → ℂ) (h : ∃ x, v x ≠ 0) : Ket d
```

**`Ket.normalize_ket_eq_self`**, a theorem, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L163). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A ket is already normalized

```lean
theorem Ket.normalize_ket_eq_self (ψ : Ket d) : Ket.normalize (ψ.vec) (Ket.exists_ne_zero ψ) = ψ
```

**`Bra.normalize`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L169).

> Create a bra out of a vector given it has a nonzero component

```lean
def Bra.normalize (v : d → ℂ) (h : ∃ x, v x ≠ 0) : Bra d
```

**`Bra.normalize_ket_eq_self`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L185).

> A bra is already normalized

```lean
lemma Bra.normalize_ket_eq_self (ψ : Bra d) : Bra.normalize (ψ.vec) (Bra.exists_ne_zero ψ) = ψ
```

**`uniform_superposition`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L192).

> Ket form by the superposition of all elements in `d`.
> Commonly denoted by |+⟩, especially for qubits

```lean
def uniform_superposition [hdne : Nonempty d] : Ket d
```

**`instInhabited`**, an instance, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L202).

> There exists a ket for every nonempty `d`.
> Here, we use the uniform superposition

```lean
instance instInhabited [Nonempty d] : Inhabited (Ket d)
```

**`Ket.basis`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L206).

> Construct the Ket corresponding to a basis vector, with a +1 phase.

```lean
def Ket.basis (i : d) : Ket d
```

**`Bra.basis`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L210).

> Construct the Bra corresponding to a basis vector, with a +1 phase.

```lean
def Bra.basis (i : d) : Bra d
```

**`instFunLikeBraket`**, an instance, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L214).

> A Bra can be viewed as a function from Ket's to ℂ.

```lean
instance instFunLikeBraket : FunLike (Bra d) (Ket d) ℂ
```

**`Braket.dot_self_eq_one`**, a theorem, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L222). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inner product of any state with itself is 1.

```lean
theorem Braket.dot_self_eq_one (ψ : Ket d) :〈ψ‖ψ〉= 1
```

**`Braket.dot_swap_conj`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L229).

> Swapping the arguments conjugates the bra-ket product:
> `⟨ψ₂|ψ₁⟩ = conj(⟨ψ₁|ψ₂⟩)`.

```lean
lemma Braket.dot_swap_conj (ψ₁ ψ₂ : Ket d) :
    〈ψ₂‖ψ₁〉 = starRingEnd ℂ 〈ψ₁‖ψ₂〉
```

**`Ket.relabel`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L239).

> Relabel a ket along an equivalence of basis index types. Given `e : d₂ ≃ d₁`,
> the amplitude of `ψ.relabel e` at `i : d₂` is the amplitude of `ψ` at `e i`.

```lean
def Ket.relabel (ψ : Ket d₁) (e : d₂ ≃ d₁) : Ket d₂
```

**`Ket.relabel_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L246).

```lean
lemma Ket.relabel_apply (ψ : Ket d₁) (e : d₂ ≃ d₁) (i : d₂) :
    ψ.relabel e i = ψ (e i)
```

**`Ket.prod`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L256).

> The outer product of two kets, creating an unentangled state.

```lean
def Ket.prod (ψ₁ : Ket d₁) (ψ₂ : Ket d₂) : Ket (d₁ × d₂)
```

**`Ket.piProd`**, a def, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L267).

> The tensor product of a finite family of kets, generalizing `Ket.prod`. Party `i` has
> basis index type `d i`, and a joint index `j` selects one index `j i` for each party; the
> amplitude at `j` is `∏ i, ψ i (j i)`.

```lean
def Ket.piProd {ι : Type*} [DecidableEq ι] [Fintype ι] {d : ι → Type*}
    [∀ i, Fintype (d i)] (ψ : (i : ι) → Ket (d i)) : Ket ((i : ι) → d i)
```

**`Ket.piProd_apply`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L276).

```lean
lemma Ket.piProd_apply {ι : Type*} [DecidableEq ι] [Fintype ι] {d : ι → Type*}
    [∀ i, Fintype (d i)] (ψ : (i : ι) → Ket (d i)) (j : (i : ι) → d i) :
    Ket.piProd ψ j = ∏ i, ψ i (j i)
```

**`Ket.IsProd`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L282).

> A Ket is a product if it's `Ket.prod` of two kets.

```lean
def Ket.IsProd (ψ : Ket (d₁ × d₂)) : Prop
```

**`Ket.IsEntangled`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L285).

> A Ket is entangled if it's not `Ket.prod` of two kets.

```lean
def Ket.IsEntangled (ψ : Ket (d₁ × d₂)) : Prop
```

**`Ket.IsProd_prod`**, a theorem, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L289). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Ket.prod` states are product states.

```lean
theorem Ket.IsProd_prod (ψ₁ : Ket d₁) (ψ₂ : Ket d₂) : (ψ₁.prod ψ₂).IsProd
```

**`Ket.not_IsEntangled_prod`**, a theorem, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L294). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Ket.prod` states are not entangled states.

```lean
theorem Ket.not_IsEntangled_prod (ψ₁ : Ket d₁) (ψ₂ : Ket d₂) : ¬(ψ₁.prod ψ₂).IsEntangled
```

**`Ket.IsProd_iff_mul_eq_mul`**, a theorem, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L298). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A ket is a product state iff its components are cross-multiplicative.

```lean
theorem Ket.IsProd_iff_mul_eq_mul (ψ : Ket (d₁ × d₂)) : ψ.IsProd ↔
    ∀ i₁ i₂ j₁ j₂, ψ (i₁,j₁)  * ψ (i₂,j₂) = ψ (i₁,j₂) * ψ (i₂,j₁)
```

**`Ket.IsPiProd`**, a def, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L365).

> A ket on the joint system of a finite family of parties is a product state if it is
> the `Ket.piProd` of one ket for each party, generalizing `Ket.IsProd`.

```lean
def Ket.IsPiProd {ι : Type*} [DecidableEq ι] [Fintype ι] {d : ι → Type*}
    [∀ i, Fintype (d i)] (ψ : Ket ((i : ι) → d i)) : Prop
```

**`Ket.isPiProd_piProd`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L371).

> Every `Ket.piProd` state satisfies `Ket.IsPiProd`, generalizing `Ket.IsProd_prod`.

```lean
lemma Ket.isPiProd_piProd {ι : Type*} [DecidableEq ι] [Fintype ι] {d : ι → Type*}
    [∀ i, Fintype (d i)] (φ : (i : ι) → Ket (d i)) : (Ket.piProd φ).IsPiProd
```

**`Ket.isPiProd_iff_isProd_relabel`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L377).

> For two parties, `Ket.IsPiProd` agrees with `Ket.IsProd` after relabeling the joint
> index type `(i : Fin 2) → d i` as `d 0 × d 1`.

```lean
lemma Ket.isPiProd_iff_isProd_relabel {d : Fin 2 → Type*} [∀ i, Fintype (d i)]
    (ψ : Ket ((i : Fin 2) → d i)) :
    ψ.IsPiProd ↔ (ψ.relabel (piFinTwoEquiv d).symm).IsProd
```

**`Ket.MES`**, a def, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L398).

> The Maximally Entangled State, or MES, on a d×d system. In principle there are many, this
> is specifically the MES with an all-positive phase. For instance on `d := Fin 2`, this is the
> Bell state.

```lean
def Ket.MES (d) [Fintype d] [Nonempty d] : Ket (d × d)
```

**`Ket.MES_isEntangled`**, a theorem, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L404). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> On any space of dimension at least two, the maximally entangled state `MES` is entangled.

```lean
theorem Ket.MES_isEntangled [Nontrivial d] : (Ket.MES d).IsEntangled
```

**`transposeTrick`**, a theorem, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L412). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The transpose trick

```lean
theorem transposeTrick {d} [Fintype d] [Nonempty d] [DecidableEq d] {M : Matrix d d ℂ} :
    (M ⊗ₖ 1) *ᵥ (Ket.MES d).vec = (1 ⊗ₖ M.transpose) *ᵥ (Ket.MES d).vec
```

**`Ket.PhaseEquiv`**, a def, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L433).

> The equivalence relation on `Ket` where two kets equivalent if they are equal up to a
> global phase, i.e. `∃ z, ‖z‖ = 1 ∧ a.vec = z • b.vec

```lean
def Ket.PhaseEquiv : Setoid (Ket d)
```

**`KetUpToPhase`**, a def, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L448).

> The type of `Ket`s up to a global phase equivalence, as given by `Ket.PhaseEquiv`.
> In particular, `MState`s really only care about a KetUpToPhase, and not Kets themselves.

```lean
def KetUpToPhase
```

**`KetUpToPhase.mk`**, a def, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L452).

> Construct a `KetUpToPhase` from a `Ket`.

```lean
def KetUpToPhase.mk (ψ : Ket d) : KetUpToPhase d
```

**`KetUpToPhase.lift`**, a def, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L456).

> Lift a function on `Ket d` to `KetUpToPhase d`, given that it respects phase equivalence.

```lean
def KetUpToPhase.lift {α : Sort*} (f : Ket d → α)
    (hf : ∀ ψ φ, Ket.PhaseEquiv.r ψ φ → f ψ = f φ) : KetUpToPhase d → α
```

**`KetUpToPhase.lift_mk`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L461).

```lean
lemma KetUpToPhase.lift_mk {α : Sort*} (f : Ket d → α)
    (hf : ∀ ψ φ, Ket.PhaseEquiv.r ψ φ → f ψ = f φ) (ψ : Ket d) :
    KetUpToPhase.lift f hf (KetUpToPhase.mk ψ) = f ψ
```

**`KetUpToPhase.ind`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L465).

```lean
lemma KetUpToPhase.ind {p : KetUpToPhase d → Prop}
    (h : ∀ ψ : Ket d, p (KetUpToPhase.mk ψ)) : ∀ q, p q
```

**`KetUpToPhase.surjective_mk`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L469).

```lean
lemma KetUpToPhase.surjective_mk : Function.Surjective (KetUpToPhase.mk (d := d))
```

**`Ket.IsPiProd.of_phaseEquiv`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L481).

> If a ket is phase-equivalent to a `Ket.IsPiProd` state, then it is also a
> `Ket.IsPiProd` state, provided there is at least one party. The global phase is
> absorbed into one tensor factor.

```lean
lemma Ket.IsPiProd.of_phaseEquiv [Nonempty ι] {ψ ψ' : Ket ((i : ι) → d i)}
    (h' : ψ'.IsPiProd) (h : Ket.PhaseEquiv.r ψ ψ') : ψ.IsPiProd
```

**`KetUpToPhase.IsPiProd`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L499).

> A ket up to global phase is a product state if its class contains a ket of the form
> `Ket.piProd φ`. If `ι` is empty, every class is a product state.

```lean
def KetUpToPhase.IsPiProd (q : KetUpToPhase ((i : ι) → d i)) : Prop
```

**`KetUpToPhase.isPiProd_mk`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L505).

> With at least one party, the class of a ket is a product state exactly when the ket
> itself is a product state.

```lean
lemma KetUpToPhase.isPiProd_mk [Nonempty ι] (ψ : Ket ((i : ι) → d i)) :
    (KetUpToPhase.mk ψ).IsPiProd ↔ ψ.IsPiProd
```

**`Ket.prod_sqrt_sum_norm_sq_eq_one`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L520).

> If the amplitudes of a ket factor as `∏ i, v i (j i)`, then the product of the norms of the
> vectors `v i` equals `1`.

```lean
lemma Ket.prod_sqrt_sum_norm_sq_eq_one {ψ : Ket ((i : ι) → d i)} {v : (i : ι) → d i → ℂ}
    (hv : ∀ j, ψ j = ∏ i, v i (j i)) : ∏ i, √(∑ a, ‖v i a‖ ^ 2) = 1
```

**`Ket.isPiProd_iff_exists_prod`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L534).

> A ket is a product state exactly when its amplitudes factor as `∏ i, v i (j i)` for some
> vectors `v i`, which need not have norm `1`.

```lean
lemma Ket.isPiProd_iff_exists_prod (ψ : Ket ((i : ι) → d i)) :
    ψ.IsPiProd ↔ ∃ v : (i : ι) → d i → ℂ, ∀ j, ψ j = ∏ i, v i (j i)
```

**`Ket.isPiProd_iff_mul_update`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L553).

> With at least one party, a ket is a product state exactly when its amplitudes satisfy the
> exchange relations, that is, when all `2 × 2` minors vanish in each flattening of its amplitude
> array that separates one party from the rest. This generalizes `Ket.IsProd_iff_mul_eq_mul`.

```lean
lemma Ket.isPiProd_iff_mul_update [Nonempty ι] (ψ : Ket ((i : ι) → d i)) :
    ψ.IsPiProd ↔ ∀ i (a b : d i) x y, ψ (Function.update x i a) * ψ (Function.update y i b) =
      ψ (Function.update x i b) * ψ (Function.update y i a)
```

## Norm bounds

**`Braket.norm_dot_le_one`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean#L585).

> The bra-ket product of normalized states has norm at most 1 (Cauchy-Schwarz).

```lean
lemma Braket.norm_dot_le_one (ψ₁ ψ₂ : Ket d) : ‖〈ψ₁‖ψ₂〉‖ ≤ 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Products of functions on a finite product](../../formathlib/exchangerelations.md)

## Sources

- [QuantumInfo/States/Pure/Braket.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/Braket.lean)
