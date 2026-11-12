---
declaration: section
origin: cited
lean: OAI.TamingCompatibility.taming_implies_compatibility
statement: formalized
proof: formalized
---

# 342. Donaldson's tamed-to-compatible conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Donaldson's tamed-to-compatible conjecture: every smooth almost complex structure on a closed four-manifold that is tamed by a symplectic form admits a compatible symplectic form. The almost complex structure stays fixed; the form's cohomology class may change.

## Taming implies compatibility on four-manifolds

We prove that every smooth almost complex structure on a closed four-manifold which is tamed by a symplectic form is compatible with a symplectic form. This gives a positive solution to Donaldson's tamed-to-compatible conjecture. We also characterize the compatible cone by strict intersection positivity on the closure of the invariant part of the taming cone.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf).

## The Lean formalization

Donaldson's tamed-to-compatible conjecture asks whether an almost-complex structure tamed by a symplectic form also admits a compatible symplectic form. The formalized result establishes this for every closed connected smooth four-manifold, keeping the almost-complex structure fixed. No integrability assumption or prescribed cohomology class for the compatible form is required.

## Lean: Taming implies compatibility

Stated in [TamingCompatibility.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TamingCompatibility.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem taming_implies_compatibility
    [T2Space X] [SecondCountableTopology X] [CompactSpace X] [ConnectedSpace X]
    (J : AlmostComplexStructure X)
    (h : ∃ α : TwoForm X, IsSymplectic α ∧ Tames α J) :
    ∃ η : TwoForm X, IsSymplectic η ∧ Compatible η J
```

Proved in [lean/OAI/Geometry/TamingCompatibility/Main.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/TamingCompatibility/Main.lean#L30).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/342.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/342.md)
