---
declaration: section
origin: cited
lean: Cslib.Turing.MultiTapeTM.TimeBoundedBy, Cslib.Turing.MultiTapeTM.SpaceBoundedBy, Cslib.Turing.MultiTapeTM.runsInSpace_of_runsInTime, Cslib.Turing.MultiTapeTM.TimeBoundedBy.spaceBoundedBy, Cslib.Turing.MultiTapeTM.Decides, Cslib.Turing.MultiTapeTM.decidableInTimeAndSpace_iff, Cslib.Turing.MultiTapeTM.DTIME, Cslib.Turing.MultiTapeTM.DSPACE
statement: formalized
proof: formalized
---

# Time and space classes on multi-tape machines

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html).

## Uniform bounds

## Time-bounded multi-tape machine

A deterministic Turing machine $M$ with $k$ work tapes
is time bounded by $t : \mathbb{N} \to \mathbb{N}$ when, for every input word $w$, every
computation path of $M$ on $w$ with at least $t(|w|)$ steps ends in a halted configuration,
where $|w|$ is the length of $w$.

Formalized by `Cslib.Turing.MultiTapeTM.TimeBoundedBy`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#time-bounded-by).

## Space-bounded multi-tape machine

A deterministic Turing machine $M$ with $k$ work tapes
is space bounded by $s : \mathbb{N} \to \mathbb{N}$ when, for every input word $w$, every
computation path of $M$ on $w$ visits at most $s(|w|)$ work-tape cells, counting the cells
visited on each work tape and summing over the tapes, where $|w|$ is the length of $w$.

Formalized by `Cslib.Turing.MultiTapeTM.SpaceBoundedBy`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#space-bounded-by).

## Time bounds space on one input

Let $M$ be a deterministic Turing machine with $k$ work
tapes, let $w$ be an input word and let $T \in \mathbb{N}$. If $M$ runs in time $T$ on $w$, that
is, every computation path of $M$ on $w$ with at least $T$ steps ends in a halted configuration,
then $M$ runs in space $k(T + 1)$ on $w$: every computation path of $M$ on $w$ visits at most
$k(T + 1)$ work-tape cells, counting the cells visited on each work tape and summing over the
tapes.

Formalized by `Cslib.Turing.MultiTapeTM.runsInSpace_of_runsInTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#runs-in-space-of-runs-in-time).

## Uniform time bounds give uniform space bounds

Let $M$ be a deterministic Turing machine
with $k$ work tapes and let $t : \mathbb{N} \to \mathbb{N}$. If $M$ is time bounded by $t$, then
$M$ is space bounded by the function $n \mapsto k(t(n) + 1)$.

Formalized by `Cslib.Turing.MultiTapeTM.TimeBoundedBy.spaceBoundedBy`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#space-bounded-by-2).

## A multi-tape machine deciding a language

A deterministic multi-tape Turing machine over
the Boolean alphabet decides a language $L$ of Boolean strings when, on every input $w$, it
eventually halts with output the one-bit string $[\mathrm{true}]$ if $w \in L$ and
$[\mathrm{false}]$ if $w \notin L$.

Formalized by `Cslib.Turing.MultiTapeTM.Decides`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#decides).

## Decidability within time and space bounds, unfolded

Let $L$ be a language of Boolean
strings and let $t$ and $s$ assign a natural number to every Boolean string. Then $L$ is decidable
within time $t$ and space $s$ in CSLib's sense, with the identity encoding of inputs, if and only
if there are a number $k$, a finite type of states and a deterministic Turing machine with $k$
work tapes over the Boolean alphabet that decides $L$ and, on every input $w$, runs in time $t(w)$
(every computation path of at least $t(w)$ steps ends in a halted configuration) and in space
$s(w)$ (every computation path visits at most $s(w)$ work-tape cells, summed over the work
tapes).

Formalized by `Cslib.Turing.MultiTapeTM.decidableInTimeAndSpace_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#decidable-in-time-and-space-iff).

## Deterministic time classes on multi-tape machines

For $t : \mathbb{N} \to \mathbb{N}$,
$\mathrm{DTIME}(t)$ is the set of languages $L$ of Boolean strings for which there are constants
$c_1, c_2 \in \mathbb{N}$, a function $s : \mathbb{N} \to \mathbb{N}$ and a deterministic
multi-tape Turing machine with Boolean tape alphabet and finitely many states such that, on every
input $w$ of length $n$, the machine halts with the one-bit output $[\mathrm{true}]$ if $w \in L$
and $[\mathrm{false}]$ otherwise, runs in time $c_1 t(n) + c_2$ (every computation path of at
least $c_1 t(n) + c_2$ steps ends in a halted configuration) and runs in space $s(n)$ (every
computation path visits at most $s(n)$ work-tape cells, summed over the work tapes).

Formalized by `Cslib.Turing.MultiTapeTM.DTIME`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#dtime).

## Deterministic space classes on multi-tape machines

For $s : \mathbb{N} \to \mathbb{N}$,
$\mathrm{DSPACE}(s)$ is the set of languages $L$ of Boolean strings for which there are constants
$c_1, c_2 \in \mathbb{N}$, a function $t : \mathbb{N} \to \mathbb{N}$ and a deterministic
multi-tape Turing machine with Boolean tape alphabet and finitely many states such that, on every
input $w$ of length $n$, the machine halts with the one-bit output $[\mathrm{true}]$ if $w \in L$
and $[\mathrm{false}]$ otherwise, runs in time $t(n)$ (every computation path of at least $t(n)$
steps ends in a halted configuration) and runs in space $c_1 s(n) + c_2$ (every computation path
visits at most $c_1 s(n) + c_2$ work-tape cells, summed over the work tapes).

Formalized by `Cslib.Turing.MultiTapeTM.DSPACE`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#dspace).

## Deterministic time classes are monotone up to affine changes of the bound

Let
$t_1, t_2 : \mathbb{N} \to \mathbb{N}$ and $a, b \in \mathbb{N}$ satisfy
$t_1(n) \le a \, t_2(n) + b$ for every $n \in \mathbb{N}$. Then
$\mathrm{DTIME}(t_1) \subseteq \mathrm{DTIME}(t_2)$.

Formalized by `Cslib.Turing.MultiTapeTM.DTIME_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#dtime-mono).

## Deterministic space classes are monotone up to affine changes of the bound

Let
$s_1, s_2 : \mathbb{N} \to \mathbb{N}$ and $a, b \in \mathbb{N}$ satisfy
$s_1(n) \le a \, s_2(n) + b$ for every $n \in \mathbb{N}$. Then
$\mathrm{DSPACE}(s_1) \subseteq \mathrm{DSPACE}(s_2)$.

Formalized by `Cslib.Turing.MultiTapeTM.DSPACE_mono`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#dspace-mono).

## Time classes are contained in space classes

For every $t : \mathbb{N} \to \mathbb{N}$,
$\mathrm{DTIME}(t) \subseteq \mathrm{DSPACE}(t)$.

Formalized by `Cslib.Turing.MultiTapeTM.DTIME_subset_DSPACE`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#dtime-subset-dspace).

## Polynomial time on multi-tape machines

$\mathrm{P}$ is the set of languages of Boolean
strings that lie in $\mathrm{DTIME}(n \mapsto n^d)$ for some $d \in \mathbb{N}$.

Formalized by `Cslib.Turing.MultiTapeTM.Classes.P`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#p).

## Polynomial space on multi-tape machines

$\mathrm{PSPACE}$ is the set of languages of
Boolean strings that lie in $\mathrm{DSPACE}(n \mapsto n^d)$ for some $d \in \mathbb{N}$.

Formalized by `Cslib.Turing.MultiTapeTM.Classes.PSPACE`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#pspace).

## P is contained in PSPACE

On the deterministic multi-tape model,
$\mathrm{P} \subseteq \mathrm{PSPACE}$.

Formalized by `Cslib.Turing.MultiTapeTM.Classes.P_subset_PSPACE`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/TimeSpace.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html#p-subset-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Time and space classes on multi-tape machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/time-and-space-classes-on-multi-tape-machines)
