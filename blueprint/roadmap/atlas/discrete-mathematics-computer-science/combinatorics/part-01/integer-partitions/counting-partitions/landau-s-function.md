---
declaration: section
origin: cited
lean: Nat.Partition.partsLCM, Nat.landauFunction, Nat.Partition.partsLCM_le_landauFunction, Nat.exists_partition_partsLCM_eq_landauFunction
statement: formalized
proof: formalized
---

# Landau's function

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html).

## Partition

## Least common multiple of the parts of a partition

For a natural number $n$ and a
partition $p$ of $n$, this is the least common multiple of the parts of $p$, taken with
the convention that it equals $1$ when $p$ has no parts.

Formalized by `Nat.Partition.partsLCM`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html#parts-lcm).

## Landau's function

For a natural number $n$, Landau's function at $n$ is the maximum, over
all partitions $p$ of $n$, of the least common multiple of the parts of $p$.

Formalized by `Nat.landauFunction`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html#landau-function).

## The Landau function bounds the LCM of the parts

For every natural number $n$ and every
partition $p$ of $n$, the least common multiple of the parts of $p$ is at most the Landau function
at $n$.

Formalized by `Nat.Partition.partsLCM_le_landauFunction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html#parts-lcm-le-landau-function).

## The Landau function is attained

For every natural number $n$, some partition of $n$
has least common multiple of its parts equal to the Landau function at $n$.

Formalized by `Nat.exists_partition_partsLCM_eq_landauFunction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/Landau.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html#exists-partition-parts-lcm-eq-landau-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Landau's function](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/landau-s-function)
