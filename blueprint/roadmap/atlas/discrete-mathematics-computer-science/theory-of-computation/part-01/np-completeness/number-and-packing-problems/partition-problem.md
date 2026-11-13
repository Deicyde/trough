---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Partition.PartitionInstance, MetaMathlibExt.Complexity.NPComplete.Partition.PartitionFeasible, MetaMathlibExt.Complexity.NPComplete.Partition.partitionDec, MetaMathlibExt.Complexity.NPComplete.Partition.partitionDec_bitEncode, MetaMathlibExt.Complexity.NPComplete.Partition.fromSubsetSum, MetaMathlibExt.Complexity.NPComplete.Partition.fromSubsetSum_feasible, MetaMathlibExt.Complexity.NPComplete.Partition.feasible_iff_doubled_sublist, MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.Phase
statement: formalized
proof: formalized
---

# Partition problem

64 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html).

## PARTITION instance as a list of naturals

A partition instance: a list of natural numbers.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.PartitionInstance`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-instance).

## Feasibility of a PARTITION instance

A sublist summing to half the total.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.PartitionFeasible`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-feasible).

## Binary-coded PARTITION decision problem

PARTITION using the canonical binary list decoder; bad framing rejects.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.partitionDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-dec).

## Binary PARTITION decider is correct on canonical encodings

A canonical encoding has exactly the intended feasibility semantics.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.partitionDec_bitEncode`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-dec-bit-encode).

## Padding map from SUBSET-SUM to PARTITION

The two padding entries in the SUBSET-SUM reduction.
No subtraction or range check is needed, even when `t > as.sum`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.fromSubsetSum`, a definition declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#from-subset-sum).

## Correctness of the SUBSET-SUM to PARTITION padding map

SUBSET-SUM reduces to PARTITION by adding two nonnegative entries.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.fromSubsetSum_feasible`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#from-subset-sum-feasible).

## PARTITION as SUBSET-SUM on the doubled list

Doubling each entry reduces PARTITION membership to SUBSET-SUM
without truncating division on odd totals.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.feasible_iff_doubled_sublist`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/Partition.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/Partition.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#feasible-iff-doubled-sublist).

## Scan phases of the PARTITION doubling pass

Reading the first marker, a later marker, or a payload bit.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.Phase`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#phase).

## Phase transition of the PARTITION doubling pass

Phase after reading one input bit.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.next`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#next).

## Output bits per input bit in the doubling pass

Output bits for one input bit; at a nonzero block prepend its low zero.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.chunk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#chunk).

## Finite-state doubling pass on raw bitstrings

The raw finite-state pass. Malformed strings have a total output too;
validation belongs to the preceding canonical decoder.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.transform`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#transform).

## Doubling pass maps a number block to the block of its double

A canonical number block becomes the canonical block of its double.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.transform_block`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#transform-block).

## Doubling pass doubles every number in a list

The stream pass doubles every number and preserves list multiplicity.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.transform_nums`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#transform-nums).

## Stacks of the PARTITION doubling machine

Input, reversed output, and output stacks of the doubling pass.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#k).

## Control labels of the PARTITION doubling machine

Three scan phases followed by reversal and a halting continuation.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#lab).

## Program of the PARTITION doubling machine

Finite-stack implementation of `transform`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#prog).

## Linear step bound for the PARTITION doubling machine

The complete pass takes at most `4 * input.length + 2` steps.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#run).

## PARTITION doubling machine as a host component

The doubling transducer as a finite component for the canonical host.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.comp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#comp).

## PARTITION doubling pass is polynomial-time

Polynomial time in the canonical bitstring encoding, from the actual
finite-state machine, including malformed raw strings.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.DoubleStream.isPolyTime_transform`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionDouble.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#is-poly-time-transform).

## Encoded reduction from SUBSET-SUM to PARTITION

SUBSET-SUM to PARTITION, with malformed inputs sent to `[1]`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.reduceFromSubsetSum`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#reduce-from-subset-sum).

## Encoded reduction from PARTITION to SUBSET-SUM

PARTITION to SUBSET-SUM, preserving the generic decoder's semantics.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.reduceToSubsetSum`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#reduce-to-subset-sum).

## Correctness of the encoded SUBSET-SUM to PARTITION reduction

The encoded reduction preserves every yes/no answer, including
malformed source strings. This is the semantic, not the time, theorem.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.reduceFromSubsetSum_correct`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#reduce-from-subset-sum-correct).

## Correctness of the encoded PARTITION to SUBSET-SUM reduction

The membership map preserves the generic decoder, including accepted
noncanonical payloads and rejected malformed framing.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.reduceToSubsetSum_correct`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionReductions.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#reduce-to-subset-sum-correct).

## Bitlength of a PARTITION sum is at most the encoded length

Summing a binary PARTITION instance cannot exceed its encoded length.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.sum_encoding_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#sum-encoding-length-le).

## Padding reduction has linear output length

The padding reduction has linear output length in its encoded input.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.fromSubsetSum_length`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#from-subset-sum-length).

## Encoded SUBSET-SUM to PARTITION map has linear output length

Linear output bound on all strings, including malformed encodings.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.reduceFromSubsetSum_length`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#reduce-from-subset-sum-length).

## PARTITION membership instance has linear bitlength

Linear bitlength bound for the membership instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.toSubsetSum_length`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionSizes.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#to-subset-sum-length).

## Stacks of the SUBSET-SUM to PARTITION padding machine

Input, reverse buffer, target, output, and unchanged sum-machine stacks.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#k-3).

## Control labels of the SUBSET-SUM to PARTITION padding machine

Parse target, preserve numbers, sum, then emit the two padding blocks.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#lab-3).

## Summation-machine stack embedding in the padding machine

The original sum component's stacks are not reimplemented.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.sumEmb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#sum-emb).

## Label map from summation halts to target emission

Both genuine sum-machine halts resume at target emission.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.sumLabel`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#sum-label).

## Program of the SUBSET-SUM to PARTITION padding machine

Padding construction by binary stack operations.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#prog-3).

## Padding machine embeds the summation machine

The host changes only the two original halting continuations.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.embeds_sum`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#embeds-sum).

## Quadratic run of the padding machine on canonical instances

The subtraction-free padding map is computed by a quadratic binary
machine on every canonical SUBSET-SUM instance, including `t > as.sum`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#run-3).

## SUBSET-SUM to PARTITION padding machine as a host component

Finite padding component for the strict source-decoding wrapper.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessCore.comp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardnessCore.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#comp-3).

## Stacks of the raw-input SUBSET-SUM to PARTITION machine

Disjoint workspaces, a preserved input, and comparison scratch stacks.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#k-2).

## Control labels of the raw-input SUBSET-SUM to PARTITION machine

Copy, exact normalization, canonicality check, and numeric computation.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#lab-2).

## Program of the raw-input SUBSET-SUM to PARTITION machine

A total finite-stack transducer for the exact source codec.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#prog-2).

## Quadratic run of the raw-input SUBSET-SUM to PARTITION machine

Total raw-input hardness reduction, with exact source rejection and
an explicit bound polynomial in encoded length, not numeric magnitude.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#run-2).

## Raw-input SUBSET-SUM to PARTITION machine as a host component

The all-string hardness reduction in the existing finite host.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.comp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#comp-2).

## SUBSET-SUM to PARTITION map is polynomial-time

The total SUBSET-SUM-to-PARTITION map is polynomial-time.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.HardnessMachine.isPolyTime_reduceFromSubsetSum`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionHardness.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#is-poly-time-reduce-from-subset-sum).

## Stacks of the canonical PARTITION membership transducer

Input, reversal buffer, and the two embedded components' stacks.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#k-5).

## Stack alphabets of the canonical PARTITION membership transducer

The summation stacks use the existing verifier alphabet.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#untitled).

## Control labels of the canonical PARTITION membership transducer

Component phases and the final sum-prefix emitter.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#lab-5).

## Summation-machine stack embedding in the membership transducer

Stack embedding of the existing sum component.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.sumEmb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#sum-emb-2).

## Doubling-machine stack embedding in the membership transducer

Stack embedding of the doubling component.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.doubleEmb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#double-emb).

## Label map from summation halts to the doubling pass

Both sum halts resume at the doubling pass.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.sumLabel`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#sum-label-2).

## Label map from the doubling halt to the prefix emitter

The doubling halt resumes at the prefix emitter.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.doubleLabel`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#double-label).

## Program of the canonical PARTITION membership transducer

Copy, sum, double, and prepend the sum, using finite-stack operations.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#prog-5).

## Membership transducer embeds the summation machine

Only genuine halts are replaced when embedding the sum machine.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.embeds_sum`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#embeds-sum-2).

## Membership transducer embeds the doubling machine

Only the doubling halt is replaced by the prefix-emitter continuation.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.embeds_double`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#embeds-double).

## Canonical PARTITION membership transducer runs in quadratic time

The canonical PARTITION membership map is computed in quadratic time
by summing, doubling, and prefixing, with no value-sized loop.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#run-5).

## Canonical PARTITION membership transducer as a host component

Finite component for normalization followed by the membership map.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipCore.comp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembershipCore.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#comp-5).

## Stacks of the raw-input PARTITION membership machine

Disjoint normalizer and numeric-core workspaces and a transfer buffer.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#k-4).

## Control labels of the raw-input PARTITION membership machine

Normalization, transfer, canonical computation, and rejection.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#lab-4).

## Normalizer workspace of the raw-input PARTITION membership machine

The exact canonicalizer's workspace.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.normEmb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#norm-emb).

## Numeric-core workspace of the raw-input PARTITION membership machine

The canonical numeric core's workspace.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.coreEmb`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#core-emb).

## Program of the raw-input PARTITION membership machine

Normalize exactly, then run the polynomial numeric core.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#prog-4).

## Raw-input PARTITION membership machine runs in quadratic time

The exact all-string membership reduction has a quadratic machine
bound, including malformed inputs and noncanonical binary payloads.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#run-4).

## Raw-input PARTITION membership machine as a host component

The total membership reduction in the existing finite host.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.comp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#comp-4).

## PARTITION to SUBSET-SUM map is polynomial-time

The total PARTITION-to-SUBSET-SUM map is polynomial-time.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.MembershipMachine.isPolyTime_reduceToSubsetSum`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#is-poly-time-reduce-to-subset-sum).

## Binary-coded PARTITION is in NP

Exact binary-coded PARTITION belongs to canonical NP.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.partitionDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionMembership.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-dec-mem-np).

## Polynomial-time reduction from SUBSET-SUM to PARTITION

Binary-coded SUBSET-SUM reduces to the exact PARTITION decision problem.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.subsetSum_polyManyOneRed_partition`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionComplete.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionComplete.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#subset-sum-poly-many-one-red-partition).

## PARTITION is NP-complete

Source: M. R. Garey and D. S. Johnson,
*Computers and Intractability* (1979), PARTITION; R. M. Karp,
"Reducibility among combinatorial problems" (1972).

Formalized by `MetaMathlibExt.Complexity.NPComplete.Partition.partition_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/PartitionComplete.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/PartitionComplete.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html#partition-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/partition-problem)
