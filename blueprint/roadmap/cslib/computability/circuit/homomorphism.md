---
catalog: module
lean: Cslib.Circuits.Homomorphism, Cslib.Circuits.Homomorphism.ext, Cslib.Circuits.Homomorphism.id, Cslib.Circuits.Homomorphism.comp, Cslib.Circuits.Homomorphism.id_map, Cslib.Circuits.Homomorphism.comp_map, Cslib.Circuits.Homomorphism.id_comp, Cslib.Circuits.Homomorphism.comp_id, Cslib.Circuits.Homomorphism.comp_assoc
statement: formalized
proof: formalized
---

# Homomorphisms of interpretations

`Cslib.Computability.Circuit.Homomorphism`, in [Cslib/Computability/Circuit/Homomorphism.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean), by Samuel Schlesinger.

> A homomorphism between two interpretations of the same signature is a map of
> carriers that commutes with every operation. This file defines identity and
> composition and proves their laws.
>
> The main use of homomorphisms in this library is that evaluation of lines,
> programs, and circuits commutes with them (`Line.map_eval`, `Program.map_eval`,
> `Program.map_trace`, and `Circuit.map_eval`).

`Cslib.Circuits.Homomorphism` (structure, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L32))

> A map that preserves every operation in a pair of interpretations.

```lean
structure Homomorphism (i₁ : Interpretation σ U₁) (i₂ : Interpretation σ U₂) where
  /-- The underlying map. -/
  map : U₁ → U₂
  /-- The map commutes with every operation in the signature. -/
  homomorphic :
    ∀ (op : σ.Op) (input : Fin (σ.Arity op) → U₁),
      map (i₁ op input) = i₂ op (map ∘ input)
```

`Cslib.Circuits.Homomorphism.ext` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L42))

```lean
theorem ext
    {source : Interpretation σ U₁}
    {target : Interpretation σ U₂}
    {left right : Homomorphism source target}
    (map_eq : left.map = right.map) : left = right
```

`Cslib.Circuits.Homomorphism.id` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L53))

> The identity map is a homomorphism.

```lean
def id (interpretation : Interpretation σ U) :
    Homomorphism interpretation interpretation
```

`Cslib.Circuits.Homomorphism.comp` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L61))

> Compose homomorphisms in the direction of their underlying maps.

```lean
def comp
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    {i₃ : Interpretation σ U₃}
    (outer : Homomorphism i₂ i₃)
    (inner : Homomorphism i₁ i₂) : Homomorphism i₁ i₃
```

`Cslib.Circuits.Homomorphism.id_map` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L73))

```lean
theorem id_map
    (interpretation : Interpretation σ U) :
    (Homomorphism.id interpretation).map = _root_.id
```

`Cslib.Circuits.Homomorphism.comp_map` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L77))

```lean
theorem comp_map
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    {i₃ : Interpretation σ U₃}
    (outer : Homomorphism i₂ i₃)
    (inner : Homomorphism i₁ i₂) :
    (outer.comp inner).map = outer.map ∘ inner.map
```

`Cslib.Circuits.Homomorphism.id_comp` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L85))

```lean
theorem id_comp
    {source : Interpretation σ U₁}
    {target : Interpretation σ U₂}
    (homomorphism : Homomorphism source target) :
    (Homomorphism.id target).comp homomorphism = homomorphism
```

`Cslib.Circuits.Homomorphism.comp_id` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L93))

```lean
theorem comp_id
    {source : Interpretation σ U₁}
    {target : Interpretation σ U₂}
    (homomorphism : Homomorphism source target) :
    homomorphism.comp (Homomorphism.id source) = homomorphism
```

`Cslib.Circuits.Homomorphism.comp_assoc` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean#L101))

```lean
theorem comp_assoc
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    {i₃ : Interpretation σ U₃}
    {i₄ : Interpretation σ U₄}
    (outer : Homomorphism i₃ i₄)
    (middle : Homomorphism i₂ i₃)
    (inner : Homomorphism i₁ i₂) :
    (outer.comp middle).comp inner = outer.comp (middle.comp inner)
```

## Depends on

- [Signatures and interpretations](signature.md)

## Sources

- [Cslib/Computability/Circuit/Homomorphism.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Homomorphism.lean)
