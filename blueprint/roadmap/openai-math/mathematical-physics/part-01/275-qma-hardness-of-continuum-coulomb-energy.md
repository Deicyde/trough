---
declaration: section
origin: cited
lean: OAI.ContinuumCoulomb.unit_coulomb_qmaHard, OAI.ContinuumCoulomb.binary_coulomb_qmaHard
statement: formalized
proof: formalized
---

# 275. QMA-hardness of continuum Coulomb energy

2 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves QMA-hardness of approximating the electronic Coulomb energy infimum in three dimensions, minimizing over the full spinful fermionic continuum space. Deterministic polynomial-time reductions work even with only unit-charge nuclei at distinct rational positions, polynomially many electrons and an energy-threshold separation of at least one.

## Continuum Coulomb hardness with binary nuclear charges

We prove that approximating the electronic Coulomb spectral infimum in three-dimensional space is QMA-hard when positive integer nuclear charges are encoded in binary. The nuclei have distinct rational positions, the electron number is unary, and the energy is minimized over all antisymmetric continuum states and spin sectors. A deterministic classical polynomial-time reduction produces instances with threshold separation at least one. The nuclear charges may be exponentially large, but every output has polynomial bit length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf); the Lean below formalizes results from it.

## QMA-hardness of continuum Coulomb energy with unit nuclear charges

We prove that approximating the electronic ground-energy infimum for clamped unit-charge nuclei is QMA-hard on the full spinful fermionic continuum space. A deterministic classical polynomial-time reduction produces polynomially many nuclei at distinct rational positions and polynomially many electrons, with polynomial rational bit lengths and threshold separation at least one. No orbital basis, magnetic field, or additional external potential is supplied, and no binding assumption is imposed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves QMA-hardness of approximating the electronic Coulomb spectral infimum in three-dimensional continuum space when positive integer nuclear charges are encoded in binary. The instances have distinct rational nuclear positions and a unary electron count, and the energy ranges over antisymmetric continuum states and all spin sectors. A deterministic polynomial-time many-one reduction produces the promise gap with threshold separation at least one, while keeping the complete output length polynomial. The same Comparator file also contains the companion unit-charge result.

The formalization proves QMA-hardness of approximating the electronic ground-energy infimum for clamped unit-charge nuclei in the full spinful fermionic continuum. The reduction is deterministic and polynomial time, with rational nuclear positions and separated rational energy thresholds. No orbital basis, magnetic field, additional external potential, or binding premise is part of the input.

The same Comparator file also includes the companion hardness result when positive integer nuclear charges are encoded in binary.

## Lean: QMA-hardness of continuum Coulomb energy with binary charges

Stated in [ContinuumCoulombHardness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContinuumCoulombHardness.lean).

```lean
theorem unit_coulomb_qmaHard : QMAHard unitCoulombCodec.encode unitCoulombPromise
```

Proved in [lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean#L14).

```lean
theorem binary_coulomb_qmaHard : QMAHard binaryCoulombCodec.encode binaryCoulombPromise
```

Proved in [lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean#L17).

## Lean: QMA-hardness of continuum Coulomb ground-energy approximation

Stated in [ContinuumCoulombHardness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContinuumCoulombHardness.lean).

```lean
theorem unit_coulomb_qmaHard : QMAHard unitCoulombCodec.encode unitCoulombPromise
```

Proved in [lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean#L14).

```lean
theorem binary_coulomb_qmaHard : QMAHard binaryCoulombCodec.encode binaryCoulombPromise
```

Proved in [lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/ContinuumCoulomb/Reduction/Hardness.lean#L17).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/275.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/275.md)
