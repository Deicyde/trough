---
declaration: module
origin: cited
lean: ConjModule, ConjModule.instModule, conjEquiv, ConjModule.involution, ConjModule.starFinsupp, Basis.conj, Basis.conj_repr_apply, Basis.conj_apply
statement: formalized
proof: formalized
---

# The conjugate module

The module `Physlib.Mathematics.Modules.ConjModule`, [Physlib/Mathematics/Modules/ConjModule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean): 9 declarations (1 instance with no name), 8 with a docstring.

> Over a commutative star-ring `k`, the *conjugate module* `ConjModule M` of a `k`-module `M` is the
> same additive group with the scalar action twisted by conjugation: `r • v := star r • v`. It turns a
> sesquilinear pairing into a bilinear one: a map conjugate-linear in a slot `M` is linear in the slot
> `ConjModule M`.
>
> `ConjModule M` is a type synonym carrying a fresh `Module k` instance (`Module.compHom` along
> `starRingEnd k`), so the twisted action does not leak onto `M` and vice versa. The canonical
> conjugate-linear identity `conjEquiv : M ≃ₛₗ[starRingEnd k] ConjModule M`, the involution
> `ConjModule (ConjModule M) ≃ₗ[k] M`, and the transported basis `Basis.conj` are provided.

## Key results

> - `ConjModule` : the conjugate-module type synonym, with its twisted `Module` instance.
> - `conjEquiv` : the canonical conjugate-linear equivalence `M ≃ₛₗ[starRingEnd k] ConjModule M`.
> - `ConjModule.involution` : the involution `ConjModule (ConjModule M) ≃ₗ[k] M`.
> - `Basis.conj` : a basis of `M` transported to a basis of `ConjModule M` (coordinates by `star`).

**`ConjModule`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L43).

> The conjugate module of `M`: the same additive group with the scalar action twisted by
> conjugation, `r • v = star r • v`. A type synonym so the twisted action stays off `M`.

```lean
def ConjModule (M : Type*)
```

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L47).

```lean
instance : AddCommGroup (ConjModule M)
```

**`ConjModule.instModule`**, an instance, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L51).

> The twisted action `r • v = star r • v`, obtained by restricting scalars along the
> conjugation ring endomorphism `starRingEnd k`.

```lean
instance instModule : Module k (ConjModule M)
```

**`conjEquiv`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L58).

> The canonical conjugate-linear equivalence `M ≃ₛₗ[starRingEnd k] ConjModule M`, the identity on
> the underlying additive group.

```lean
def conjEquiv : M ≃ₛₗ[starRingEnd k] ConjModule M
```

**`ConjModule.involution`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L71).

> Conjugating twice returns the original module: the `k`-linear isomorphism
> `ConjModule (ConjModule M) ≃ₗ[k] M`. It is `k`-linear, not merely semilinear, because
> `starRingEnd k` composed with itself is the identity.

```lean
def involution : ConjModule (ConjModule M) ≃ₗ[k] M
```

**`ConjModule.starFinsupp`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L77).

> Coordinate-wise conjugation on `ι →₀ k`, a conjugate-linear self-equivalence.

```lean
noncomputable def starFinsupp : (ι →₀ k) ≃ₛₗ[starRingEnd k] (ι →₀ k)
```

**`Basis.conj`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L90).

> A basis of `M` transported to a basis of `ConjModule M`: the same basis vectors, with
> coordinates conjugated (`(Basis.conj b).repr v = star ∘ b.repr v`).

```lean
noncomputable def _root_.Basis.conj (b : Basis ι k M) : Basis ι k (ConjModule M)
```

**`Basis.conj_repr_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L95).

> Coordinates in `Basis.conj b` are the `star` of the coordinates in `b`.

```lean
lemma _root_.Basis.conj_repr_apply (b : Basis ι k M) (v : ConjModule M) (i : ι) :
    (Basis.conj b).repr v i = star (b.repr ((conjEquiv (k := k) (M := M)).symm v) i)
```

**`Basis.conj_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean#L99).

> The basis vectors of `Basis.conj b` are those of `b`, viewed through `conjEquiv`.

```lean
lemma _root_.Basis.conj_apply (b : Basis ι k M) (i : ι) :
    Basis.conj b i = conjEquiv (k := k) (M := M) (b i)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Modules/ConjModule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/ConjModule.lean)
