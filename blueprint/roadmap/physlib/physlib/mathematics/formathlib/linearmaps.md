---
declaration: module
origin: cited
lean: HomogeneousQuadratic, HomogeneousQuadratic.instFun, HomogeneousQuadratic.map_smul, BiLinearSymm, IsSymmetric, BiLinearSymm.instFun, BiLinearSymm.mk₂, BiLinearSymm.map_smul₁
statement: formalized
proof: formalized
---

# Linear maps

The module `Physlib.Mathematics.ForMathlib.LinearMaps`, [Physlib/Mathematics/ForMathlib/LinearMaps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean): 41 declarations, 15 with a docstring.

> Some definitions and properties of linear, bilinear, and trilinear maps, along with homogeneous
> quadratic and cubic equations.

**`HomogeneousQuadratic`**, a def, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L23).

> The structure defining a homogeneous quadratic equation.

```lean
def HomogeneousQuadratic (V : Type) [AddCommMonoid V] [Module ℚ V] : Type
```

**`HomogeneousQuadratic.instFun`**, an instance, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L31).

> A homogeneous quadratic equation can be treated as a function from `V` to `ℚ`.

```lean
instance instFun : FunLike (HomogeneousQuadratic V) V ℚ
```

**`HomogeneousQuadratic.map_smul`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L38).

```lean
lemma map_smul (f : HomogeneousQuadratic V) (a : ℚ) (S : V) : f (a • S) = a ^ 2 * f S
```

**`BiLinearSymm`**, a structure, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L44).

> The structure of a symmetric bilinear function.

```lean
structure BiLinearSymm (V : Type) [AddCommMonoid V] [Module ℚ V] extends V →ₗ[ℚ] V →ₗ[ℚ] ℚ where
  swap' : ∀ S T, toFun S T = toFun T S
```

**`IsSymmetric`**, a class, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L48).

> A symmetric bilinear function.

```lean
class IsSymmetric {V : Type} [AddCommMonoid V] [Module ℚ V] (f : V →ₗ[ℚ] V →ₗ[ℚ] ℚ) : Prop where
  swap : ∀ S T, f S T = f T S
```

**`BiLinearSymm.instFun`**, an instance, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L57).

> A symmetric bilinear form can be treated as a function from `V` to `V →ₗ[ℚ] ℚ`.

```lean
instance instFun (V : Type) [AddCommMonoid V] [Module ℚ V] :
    FunLike (BiLinearSymm V) V (V →ₗ[ℚ] ℚ)
```

**`BiLinearSymm.mk₂`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L68).

> The construction of a symmetric bilinear map from `smul` and `map_add` in the first factor,
> and swap.

```lean
def mk₂ (f : V × V → ℚ) (map_smul : ∀ a S T, f (a • S, T) = a * f (S, T))
    (map_add : ∀ S1 S2 T, f (S1 + S2, T) = f (S1, T) + f (S2, T))
    (swap : ∀ S T, f (S, T) = f (T, S)) : BiLinearSymm V
```

**`BiLinearSymm.map_smul₁`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L87).

```lean
lemma map_smul₁ (f : BiLinearSymm V) (a : ℚ) (S T : V) : f (a • S) T = a * f S T
```

**`BiLinearSymm.swap`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L92).

```lean
lemma swap (f : BiLinearSymm V) (S T : V) : f S T = f T S
```

**`BiLinearSymm.map_smul₂`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L94).

```lean
lemma map_smul₂ (f : BiLinearSymm V) (a : ℚ) (S : V) (T : V) : f S (a • T) = a * f S T
```

**`BiLinearSymm.map_add₁`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L97).

```lean
lemma map_add₁ (f : BiLinearSymm V) (S1 S2 T : V) : f (S1 + S2) T = f S1 T + f S2 T
```

**`BiLinearSymm.map_add₂`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L102).

```lean
lemma map_add₂ (f : BiLinearSymm V) (S : V) (T1 T2 : V) :
    f S (T1 + T2) = f S T1 + f S T2
```

**`BiLinearSymm.toLinear₁`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L107).

> Fixing the second input vectors, the resulting linear map.

```lean
def toLinear₁ (f : BiLinearSymm V) (T : V) : V →ₗ[ℚ] ℚ
```

**`BiLinearSymm.toLinear₁_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L112).

```lean
lemma toLinear₁_apply (f : BiLinearSymm V) (S T : V) : f S T = f.toLinear₁ T S
```

**`BiLinearSymm.map_sum₁`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L114).

```lean
lemma map_sum₁ {n : ℕ} (f : BiLinearSymm V) (S : Fin n → V) (T : V) :
    f (∑ i, S i) T = ∑ i, f (S i) T
```

**`BiLinearSymm.map_sum₂`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L118).

```lean
lemma map_sum₂ {n : ℕ} (f : BiLinearSymm V) (S : Fin n → V) (T : V) :
    f T (∑ i, S i) = ∑ i, f T (S i)
```

**`BiLinearSymm.toHomogeneousQuad`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L123).

> The homogeneous quadratic equation obtainable from a bilinear function.

```lean
def toHomogeneousQuad {V : Type} [AddCommMonoid V] [Module ℚ V]
    (τ : BiLinearSymm V) : HomogeneousQuadratic V
```

**`BiLinearSymm.toHomogeneousQuad_add`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L131).

```lean
lemma toHomogeneousQuad_add {V : Type} [AddCommMonoid V] [Module ℚ V]
    (τ : BiLinearSymm V) (S T : V) :
    τ.toHomogeneousQuad (S + T) = τ.toHomogeneousQuad S +
    τ.toHomogeneousQuad T + 2 * τ S T
```

**`HomogeneousCubic`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L142).

> The structure of a homogeneous cubic equation.

```lean
def HomogeneousCubic (V : Type) [AddCommMonoid V] [Module ℚ V] : Type
```

**`HomogeneousCubic.instFun`**, an instance, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L150).

> A homogeneous cubic equation can be treated as a function from `V` to `ℚ`.

```lean
instance instFun : FunLike (HomogeneousCubic V) V ℚ
```

**`HomogeneousCubic.map_smul`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L157).

```lean
lemma map_smul (f : HomogeneousCubic V) (a : ℚ) (S : V) : f (a • S) = a ^ 3 * f S
```

**`TriLinearSymm`**, a structure, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L163).

> The structure of a symmetric trilinear function.

```lean
structure TriLinearSymm (V : Type) [AddCommMonoid V] [Module ℚ V] extends
    V →ₗ[ℚ] V →ₗ[ℚ] V →ₗ[ℚ] ℚ where
  swap₁' : ∀ S T L, toFun S T L = toFun T S L
  swap₂' : ∀ S T L, toFun S T L = toFun S L T
```

**`TriLinearSymm.instFun`**, an instance, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L173).

> A symmetric trilinear form can be treated as a function from `V` to `V →ₗ[ℚ] V →ₗ[ℚ] ℚ`.

```lean
instance instFun : FunLike (TriLinearSymm V) V (V →ₗ[ℚ] V →ₗ[ℚ] ℚ)
```

**`TriLinearSymm.mk₃`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L183).

> The construction of a symmetric trilinear map from `smul` and `map_add` in the first factor,
> and two swap.

```lean
def mk₃ (f : V × V × V→ ℚ) (map_smul : ∀ a S T L, f (a • S, T, L) = a * f (S, T, L))
    (map_add : ∀ S1 S2 T L, f (S1 + S2, T, L) = f (S1, T, L) + f (S2, T, L))
    (swap₁ : ∀ S T L, f (S, T, L) = f (T, S, L))
    (swap₂ : ∀ S T L, f (S, T, L) = f (S, L, T)) : TriLinearSymm V
```

**`TriLinearSymm.swap₁`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L201).

```lean
lemma swap₁ (f : TriLinearSymm V) (S T L : V) : f S T L = f T S L
```

**`TriLinearSymm.swap₂`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L204).

```lean
lemma swap₂ (f : TriLinearSymm V) (S T L : V) : f S T L = f S L T
```

**`TriLinearSymm.swap₃`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L207).

```lean
lemma swap₃ (f : TriLinearSymm V) (S T L : V) : f S T L = f L T S
```

**`TriLinearSymm.map_smul₁`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L210).

```lean
lemma map_smul₁ (f : TriLinearSymm V) (a : ℚ) (S T L : V) :
    f (a • S) T L = a * f S T L
```

**`TriLinearSymm.map_smul₂`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L216).

```lean
lemma map_smul₂ (f : TriLinearSymm V) (S : V) (a : ℚ) (T L : V) :
    f S (a • T) L = a * f S T L
```

**`TriLinearSymm.map_smul₃`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L220).

```lean
lemma map_smul₃ (f : TriLinearSymm V) (S T : V) (a : ℚ) (L : V) :
    f S T (a • L) = a * f S T L
```

**`TriLinearSymm.map_add₁`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L224).

```lean
lemma map_add₁ (f : TriLinearSymm V) (S1 S2 T L : V) :
    f (S1 + S2) T L = f S1 T L + f S2 T L
```

**`TriLinearSymm.map_add₂`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L230).

```lean
lemma map_add₂ (f : TriLinearSymm V) (S T1 T2 L : V) :
    f S (T1 + T2) L = f S T1 L + f S T2 L
```

**`TriLinearSymm.map_add₃`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L234).

```lean
lemma map_add₃ (f : TriLinearSymm V) (S T L1 L2 : V) :
    f S T (L1 + L2) = f S T L1 + f S T L2
```

**`TriLinearSymm.toLinear₁`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L239).

> Fixing the second and third input vectors, the resulting linear map.

```lean
def toLinear₁ (f : TriLinearSymm V) (T L : V) : V →ₗ[ℚ] ℚ
```

**`TriLinearSymm.toLinear₁_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L246).

```lean
lemma toLinear₁_apply (f : TriLinearSymm V) (S T L : V) : f S T L = f.toLinear₁ T L S
```

**`TriLinearSymm.map_sum₁`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L248).

```lean
lemma map_sum₁ {n : ℕ} (f : TriLinearSymm V) (S : Fin n → V) (T : V) (L : V) :
    f (∑ i, S i) T L = ∑ i, f (S i) T L
```

**`TriLinearSymm.map_sum₂`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L253).

```lean
lemma map_sum₂ {n : ℕ} (f : TriLinearSymm V) (S : Fin n → V) (T : V) (L : V) :
    f T (∑ i, S i) L = ∑ i, f T (S i) L
```

**`TriLinearSymm.map_sum₃`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L258).

```lean
lemma map_sum₃ {n : ℕ} (f : TriLinearSymm V) (S : Fin n → V) (T : V) (L : V) :
    f T L (∑ i, S i) = ∑ i, f T L (S i)
```

**`TriLinearSymm.map_sum₁₂₃`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L261).

```lean
lemma map_sum₁₂₃ {n1 n2 n3 : ℕ} (f : TriLinearSymm V) (S : Fin n1 → V)
    (T : Fin n2 → V) (L : Fin n3 → V) :
    f (∑ i, S i) (∑ i, T i) (∑ i, L i) = ∑ i, ∑ k, ∑ l, f (S i) (T k) (L l)
```

**`TriLinearSymm.toCubic`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L271).

> The homogeneous cubic equation obtainable from a symmetric trilinear function.

```lean
def toCubic {charges : Type} [AddCommMonoid charges] [Module ℚ charges]
    (τ : TriLinearSymm charges) : HomogeneousCubic charges
```

**`TriLinearSymm.toCubic_add`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean#L280).

```lean
lemma toCubic_add {charges : Type} [AddCommMonoid charges] [Module ℚ charges]
    (τ : TriLinearSymm charges) (S T : charges) :
    τ.toCubic (S + T) = τ.toCubic S +
    τ.toCubic T + 3 * τ S S T + 3 * τ T T S
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/LinearMaps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/LinearMaps.lean)
