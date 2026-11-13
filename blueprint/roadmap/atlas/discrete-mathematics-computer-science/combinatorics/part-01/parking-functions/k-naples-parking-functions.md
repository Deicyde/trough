---
declaration: section
origin: cited
lean: MetaMathlibExt.naplesSpot, MetaMathlibExt.naplesPark, MetaMathlibExt.IsNaplesParkingFunction, MetaMathlibExt.naplesPark_example, MetaMathlibExt.isNaplesParkingFunction_example, MetaMathlibExt.ascendingNaplesCount, MetaMathlibExt.ascendingNaplesOneCount, MetaMathlibExt.descendingNaplesCount
statement: formalized
---

# k-Naples parking functions

42 results, 25 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html).

## The $k$-Naples rule

On the spots $1, \dots, n$, when the spots in a list $O$ of natural
numbers are occupied, a car preferring $a$ parks in $a$ if $a$ is free; otherwise in the first
free spot among those of $a - 1, \dots, a - k$ that are at least $1$, checked in decreasing
order; otherwise in the first free spot among $a + 1, \dots, n$, checked in increasing order.
The car cannot park if none of these is free, or if $a$ is not one of the spots $1, \dots, n$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 1.

Formalized by `MetaMathlibExt.naplesSpot`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-spot).

## Naples parking

Starting from a list of occupied spots, cars with preferences
$a_1, \dots, a_m \in \mathbb{N}$ arrive in order, and each takes the spot given by the $k$-Naples
rule on the spots $1, \dots, n$ for the spots occupied when it arrives. If every car parks, the
result is the final list of occupied spots: the spots of the cars, most recent first, followed by
the initially occupied spots. If some car cannot park, there is no result.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 1.

Formalized by `MetaMathlibExt.naplesPark`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park).

## $k$-Naples parking function

A preference $\alpha = (a_1, \dots, a_n)$ of length $n$
is a $k$-Naples parking function if $1 \le a_i \le n$ for every $i$ and all $n$ cars park on
the spots $1, \dots, n$ when they arrive in order and follow the $k$-Naples rule: car $i$ takes
spot $a_i$ if it is free; otherwise the first free spot among $a_i - 1, \dots, a_i - k$, checked
in decreasing order and only among spots at least $1$; otherwise the first free spot after
$a_i$, if there is one. For $k = 0$ these are the ordinary parking functions.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 1.

Formalized by `MetaMathlibExt.IsNaplesParkingFunction`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-naples-parking-function).

## A $2$-Naples parking example

Under the $2$-Naples rule on the spots $1, \dots, 7$, the
cars with preferences $(6, 6, 6, 5, 5, 2, 1)$, arriving in order into an empty lot, all park, in
the spots $6, 5, 4, 3, 7, 2, 1$ respectively.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 1.

Formalized by `MetaMathlibExt.naplesPark_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-example).

## A $2$-Naples parking function that is not $1$-Naples

The preference
$(6, 6, 6, 5, 5, 2, 1)$ of length $7$ is a $2$-Naples parking function but not a $1$-Naples
parking function.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 1.

Formalized by `MetaMathlibExt.isNaplesParkingFunction_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-naples-parking-function-example).

## Number of ascending $k$-Naples parking functions

For natural numbers $n$ and $k$,
$I_{n,k}$ is the number of $k$-Naples parking functions $(a_1, \dots, a_n)$ of length $n$ that
are weakly increasing, that is, $a_1 \le a_2 \le \dots \le a_n$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 3.

Formalized by `MetaMathlibExt.ascendingNaplesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-count).

## Number of ascending $k$-Naples parking functions starting with $1$

For natural numbers
$n$ and $k$, $U_{n,k}$ is the number of weakly increasing $k$-Naples parking functions
$(a_1, \dots, a_n)$ of length $n$ with $a_1 = 1$; in particular $U_{0,k} = 0$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 3.

Formalized by `MetaMathlibExt.ascendingNaplesOneCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-one-count).

## Number of descending $k$-Naples parking functions

For natural numbers $n$ and $k$, this
is the number of $k$-Naples parking functions $\alpha = (a_1, \dots, a_n)$ of length $n$ (so
$a_i \in \{1, \dots, n\}$ for all $i$) that are descending, that is, weakly decreasing:
$a_1 \ge a_2 \ge \dots \ge a_n$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 2.

Formalized by `MetaMathlibExt.descendingNaplesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-naples-count).

## Number of descending strictly $k$-Naples parking functions

For natural numbers $n$ and
$k$, this is the number of preferences $\alpha = (a_1, \dots, a_n) \in \{1, \dots, n\}^n$ that
are descending ($a_1 \ge a_2 \ge \dots \ge a_n$), are $k$-Naples parking functions, and are not
$(k - 1)$-Naples parking functions. It is used for $k \ge 1$; for $k = 0$, where $k - 1$ is
read as $0$, the count is $0$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 4.

Formalized by `MetaMathlibExt.descendingStrictNaplesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-strict-naples-count).

## Naples counts for $n = 2$ and $k = 1$

Among the preferences of length $2$ with entries
in $\{1, 2\}$, exactly $3$ are weakly increasing $1$-Naples parking functions ($I_{2,1} = 3$),
and exactly $2$ of these start with $1$ ($U_{2,1} = 2$); exactly $3$ are weakly decreasing
$1$-Naples parking functions, and exactly $1$ is weakly decreasing, $1$-Naples and not
$0$-Naples.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 4.

Formalized by `MetaMathlibExt.naplesCount_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-count-two-one).

## Height of a lattice path

For a lattice path $p$ of $m$ steps, each an Up step $(1, 1)$
or a Down step $(1, -1)$, and a natural number $j$, the height of $p$ after $j$ steps is the
number of Up steps minus the number of Down steps among the first $\min(j, m)$ steps of $p$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3.

Formalized by `MetaMathlibExt.latticeHeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#lattice-height).

## Height of a sequence of Dyck steps

For a finite sequence $l$ of Up steps $U$ and Down
steps $D$ and a natural number $j$, the height of $l$ after $j$ steps is the integer obtained as
the number of $U$ minus the number of $D$ among the first $j$ steps of $l$ (among all of $l$
when $j$ exceeds its length).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3.

Formalized by `MetaMathlibExt.dyckStepHeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#dyck-step-height).

## $k$-Dyck path

Let $n$ and $k$ be natural numbers. A lattice path of $2n$ steps, each
an Up step $(1, 1)$ or a Down step $(1, -1)$, is a $k$-Dyck path of semilength $n$ if its height
after all $2n$ steps is $0$, its height after its first $j$ steps is at least $-k$ for every
$j \le 2n$, and, when $n \ge 1$, its last step is a Down step.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3.

Formalized by `MetaMathlibExt.IsKDyckPath`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-kdyck-path).

## A $1$-Dyck path that is not a $0$-Dyck path

Write $U$ for an Up step $(1, 1)$ and $D$
for a Down step $(1, -1)$. The path $DUUD$ is a $1$-Dyck path of semilength $2$ but not a
$0$-Dyck path, and the path $UUD$ has height $1$ after its three steps.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3.

Formalized by `MetaMathlibExt.isKDyckPath_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-kdyck-path-example).

## Every $k$-Naples parking function is $(k + 1)$-Naples

For all natural numbers $k$
and $n$, every $k$-Naples parking function $\alpha$ of length $n$ is also a $(k + 1)$-Naples
parking function.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 1.

Stated but not proved: `MetaMathlibExt.IsNaplesParkingFunction.succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#succ).

## The $k$-Naples rule on $\mathbb{Z}$

When the spots in a finite list $O$ of integers are
occupied, a car preferring $a \in \mathbb{Z}$ parks in $a$ if $a$ is free; otherwise in the first
free spot among $a - 1, \dots, a - k$, checked in decreasing order with no lower bound; otherwise
in the first free spot among $a + 1, \dots, a + |O| + 1$, checked in increasing order (one of
them is free, so this is the first free spot after $a$).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 2 (parking on `ℤ`).

Formalized by `MetaMathlibExt.naplesSpotInt`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-spot-int).

## Naples parking on $\mathbb{Z}$

Starting from a list of occupied spots in $\mathbb{Z}$,
cars with integer preferences $a_1, \dots, a_m$ arrive in order, and each takes the spot given by
the $k$-Naples rule on $\mathbb{Z}$ for the spots occupied when it arrives. The result is the
final list of occupied spots: the spots of the cars, most recent first, followed by the initially
occupied spots.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 2 (parking on `ℤ`).

Formalized by `MetaMathlibExt.naplesParkInt`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-int).

## A $2$-Naples parking example on $\mathbb{Z}$

Under the $2$-Naples rule on $\mathbb{Z}$,
the cars with preferences $(4, 2, 2, 2)$, arriving in order with no spot occupied, park in the
spots $4, 2, 1, 0$ respectively.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 2, Figure 1.

Formalized by `MetaMathlibExt.naplesParkInt_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-int-example).

## A $3$-Naples parking example on $\mathbb{Z}$

Under the $3$-Naples rule on $\mathbb{Z}$,
the cars with preferences $(1, 2, 2, 5, 7, 7, 7, 3)$, arriving in order with no spot occupied,
park in the spots $1, 2, 0, 5, 7, 6, 4, 3$ respectively.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 2, Remark 2.

Formalized by `MetaMathlibExt.naplesParkInt_example_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-int-example-three).

## One more backward step keeps the cars in $\{0, \dots, n\}$

Let $(a_1, \dots, a_n)$ be
integers with $1 \le a_j \le n$ for every $j$. If, under the $k$-Naples rule on $\mathbb{Z}$, the
cars with these preferences, arriving in order with no spot occupied, occupy exactly the spots
$1, \dots, n$, then under the $(k + 1)$-Naples rule on $\mathbb{Z}$ every car parks in a spot $s$
with $0 \le s \le n$.

Every $k \ge 0$ is admitted (the source's proof treats any $k \ge 0$).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Lemma 1.

Stated but not proved: `MetaMathlibExt.naplesParkInt_succ_mem_Icc` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-int-succ-mem-icc).

## Descending $k$-Naples parking functions and $k$-Dyck paths

For all natural numbers
$n \ge 1$ and $k \ge 1$, the number of weakly decreasing $k$-Naples parking functions of length
$n$ equals the number of $k$-Dyck paths of length $n$: sequences of $2n$ Up and Down steps that
end at height $0$, never go below height $-k$, and end with a Down step.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 2 (citing Christensen et al., Theorem 1.3).

Stated but not proved: `MetaMathlibExt.descendingNaplesCount_eq_card_kDyckPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-naples-count-eq-card-k-dyck-p).

## Descending $k$-Naples parking functions and Dyck paths

For all natural numbers $n \ge 1$
and $k \ge 1$, the number of weakly decreasing $k$-Naples parking functions of length $n$ equals
the number of Dyck paths of semilength $n + k$ (that is, with $2(n + k)$ steps) whose first $k$
steps are Up and whose last $k + 1$ steps are Down.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 3.

Stated but not proved: `MetaMathlibExt.descendingNaplesCount_eq_card_dyckPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-naples-count-eq-card-dyck-pat).

## Descending strictly $k$-Naples parking functions and Dyck paths with an early return

For $n \ge 1$ and $k \ge 1$, the number of descending strictly $k$-Naples parking functions of
length $n$ (descending preferences that are $k$-Naples but not $(k - 1)$-Naples) equals the
number of Dyck paths of semilength $n + k$, that is, with $2(n + k)$ Up and Down steps, whose
first $k$ steps are Up, whose last $k + 1$ steps are Down, and whose height after $j$ steps is
$0$ for some $j$ with $0 < j < 2(n + k)$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 4.

Stated but not proved: `MetaMathlibExt.descendingStrictNaplesCount_eq_card_dyckPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-strict-naples-count-eq-card-d).

## Recurrence for ascending $k$-Naples parking functions

Let $I_{n,k}$ be the number of
weakly increasing $k$-Naples parking functions of length $n$, let $U_{n,k}$ be the number of
those whose first entry is $1$, and let $C_k$ be the $k$-th Catalan number. For all natural
numbers $n$ and $k$ with $1 \le k \le n - 1$,

$$I_{n,k} = I_{n,k-1} + C_k \sum_{i=0}^{n-k} I_{i,k-1} \, U_{n-k-i,k}$$

and

$$U_{n,k} = U_{n,k-1} + C_k \sum_{i=0}^{n-k} U_{i,k-1} \, U_{n-k-i,k}.$$

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 3.

Stated but not proved: `MetaMathlibExt.ascendingNaplesCount_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-count-recurrence).

## Ascending $1$-Naples parking functions starting with $1$ and Fine numbers

For every
natural number $n$, the number $U_{n,1}$ of weakly increasing $1$-Naples parking functions of
length $n$ whose first entry is $1$ equals the Fine number $F(n + 1)$, where the Fine numbers
$1, 0, 1, 2, 6, 18, \dots$ are indexed so that $F(0) = 1$ and $F(1) = 0$ (OEIS A000957).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 4.

Stated but not proved: `MetaMathlibExt.ascendingNaplesOneCount_one_eq_fineNumber` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-one-count-one-eq-fine-n).

## Counting ascending $1$-Naples parking functions

For every natural number $n$, let
$I_{n,1}$ be the number of weakly increasing $1$-Naples parking functions of length $n$. Then

$$I_{n,1} = \sum_{i=0}^{n} C_i \, F(n - i),$$

where $C_i$ is the $i$-th Catalan number and $F$ is the sequence of Fine numbers, indexed so that
$F(0) = 1$ and $F(1) = 0$. This is the convolution of the Catalan and Fine numbers (OEIS A000958).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 5.

Stated but not proved: `MetaMathlibExt.ascendingNaplesCount_one_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-count-one-eq-sum).

## Generating functions for ascending $k$-Naples parking functions

Let $I_{n,k}$ be the
number of weakly increasing $k$-Naples parking functions of length $n$, let $U_{n,k}$ be the
number of those whose first entry is $1$, and let $C_k$ be the $k$-th Catalan number. Write
$I_k(x) = \sum_{n \ge 0} I_{n,k} x^n$ and $U_k(x) = \sum_{n \ge 0} U_{n,k} x^n$, formal power
series with natural number coefficients. For every natural number $k \ge 1$,

$$I_k(x) = I_{k-1}(x) + C_k x^k I_{k-1}(x) U_k(x)$$

and

$$U_k(x) = U_{k-1}(x) + C_k x^k U_{k-1}(x) U_k(x).$$

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 6.

Stated but not proved: `MetaMathlibExt.ascendingNaples_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-generating-function).

## Counting descending $k$-Naples parking functions

For all natural numbers $n \ge 1$ and
$k \ge 1$, the number of weakly decreasing $k$-Naples parking functions of length $n$ is
$\binom{2n-1}{n} - \binom{2n-1}{n+k+1}$, and the number of weakly decreasing strictly
$k$-Naples parking functions of length $n$ (those that are $k$-Naples but not $(k-1)$-Naples)
is $\frac{k+1}{n} \binom{2n}{n+k+1}$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 7.

Stated but not proved: `MetaMathlibExt.descendingNaplesCount_eq_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-naples-count-eq-choose).

## Lattice path of a parking preference

Let $\alpha = (a_1, \dots, a_n)$ be a sequence of
natural numbers. Its lattice path is the sequence of $2n$ steps, each an Up step $(1, 1)$ or a
Down step $(1, -1)$, obtained by taking, for each spot $s = 1, \dots, n$ in turn, one Up step
for every index $i$ with $a_i = s$ followed by one Down step, and then appending Down steps
until there are $2n$ steps. When every $a_i$ lies in $\{1, \dots, n\}$ this gives exactly $2n$
steps and nothing is appended; if moreover $\alpha$ is weakly increasing, the $i$-th Up step is
preceded by exactly $a_i - 1$ Down steps.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3 (Remark 3.3).

Formalized by `MetaMathlibExt.preferencePath`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#preference-path).

## The lattice path of $(1, 3, 3, 5, 6, 6)$

The lattice path of the parking preference
$(1, 3, 3, 5, 6, 6)$ is $\mathrm{UDDUUDDUDUUD}$, where $\mathrm{U}$ is an Up step and
$\mathrm{D}$ a Down step.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 3 (Figure 3).

Formalized by `MetaMathlibExt.preferencePath_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#preference-path-example).

## Remaining cars still park after moving a car to an earlier spot

Let $(a_1, \dots, a_n)$
be a parking preference with $1 \le a_j \le n$ for every $j$, with which all $n$ cars, arriving in
order into an empty lot, park under the $k$-Naples rule on the spots $1, \dots, n$, car $j$ in
spot $d_j$. Let $1 \le l \le i \le n$, and let $q$ be a spot with $1 \le q < d_l$ and $q \ne d_j$
for every $j \le i$ with $j \ne l$. If exactly the spots $d_1, \dots, d_i$, with $d_l$ replaced
by $q$, are occupied, then the remaining cars $a_{i+1}, \dots, a_n$, arriving in order, all park
under the $k$-Naples rule.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.naplesPark_drop_set_isSome` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#naples-park-drop-set-is-some).

## Lattice-path criterion for ascending $k$-Naples parking functions

Let
$\alpha = (a_1, \dots, a_n)$ be a weakly increasing preference with $1 \le a_i \le n$ for every
$i$, and let $h_j$ be the height after the first $j$ steps of the lattice path of $\alpha$, which
has $2n$ steps. Then $\alpha$ is a $k$-Naples parking function if and only if for every $j$
with $1 \le j \le 2n$ and $h_j < 0$ there is a $j'$ with $j < j' \le j + 2k$, $j' \le 2n$ and
$h_{j'} > 0$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 2.6 (published as Theorem 2).

Stated but not proved: `MetaMathlibExt.isNaplesParkingFunction_iff_of_monotone` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-naples-parking-function-iff-of-monoto).

## When every rearrangement of a preference is $k$-Naples

Let
$\alpha = (a_1, \dots, a_n) \in \{1, \dots, n\}^n$ and let $P$ be its lattice path: for each
spot $s = 1, \dots, n$ in turn, one Up step for every car preferring $s$, then one Down step
(this is also the lattice path of the ascending rearrangement of $\alpha$). The height of $P$
after $m$ steps is the number of Up steps minus the number of Down steps among its first $m$
steps. Then every rearrangement of $\alpha$ is a $k$-Naples parking function if and only if,
for every $i$ with $1 \le i \le 2n$ such that the height of $P$ after $i$ steps is negative,
there is a $j$ with $i < j \le i + 2k$ and $j \le 2n$ such that the height of $P$ after $j$
steps is positive.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Corollary 2.7 (published as Corollary 1).

Stated but not proved: `MetaMathlibExt.forall_perm_isNaplesParkingFunction_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#forall-perm-is-naples-parking-function-i).

## Ascending $k$-Naples parking functions and Dyck paths

For all natural numbers $n \ge 1$
and $k$, the number of weakly increasing $k$-Naples parking functions of length $n$ equals the
number of Dyck paths of semilength $n + k$ (that is, with $2(n + k)$ steps) whose first $k$ steps
are Up, whose last $k + 1$ steps are Down, and which satisfy the following condition. Writing
$h_j$ for the height after the first $j$ steps, whenever the $m$-th step is a Down step that is
not among the last $k + 1$ steps and $h_m < k$, there is a $j$ with $m < j \le m + 2k$ and
$j \le 2(n + k)$ such that $h_j > k$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Corollary 2.12 (published as Corollary 3).

Stated but not proved: `MetaMathlibExt.ascendingNaplesCount_eq_card_dyckPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#ascending-naples-count-eq-card-dyck-path).

## Left spine length of a binary tree

The number of nodes on the left spine of a binary tree: the root, its left child, that
child's left child, and so on (`0` for the empty tree).

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 4 (Proposition 4.12).

Formalized by `MetaMathlibExt.leftSpineLength`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#left-spine-length).

## Left spine lengths of small binary trees

The empty binary tree has left spine length
$0$, and the binary tree with three nodes, a root whose left child and right child have no
children, has left spine length $2$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 4 (Proposition 4.12).

Formalized by `MetaMathlibExt.leftSpineLength_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#left-spine-length-examples).

## Descending strictly $k$-Naples parking functions and binary trees

For every $n$ and
every $k \ge 1$, the number of descending strictly $k$-Naples parking functions of length $n$
(descending preferences that are $k$-Naples but not $(k - 1)$-Naples) equals the number of
binary trees $t$ with $n + k$ nodes such that the left spine of $t$ (the root, its left child,
that child's left child, and so on) has at least $k$ nodes and the left spine of the right
subtree of $t$ has at least $k + 1$ nodes.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Proposition 4.12 (published as Proposition 5).

Stated but not proved: `MetaMathlibExt.descendingStrictNaplesCount_eq_card_binaryTree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-strict-naples-count-eq-card-b).

## Edges of an inscribed polygon

Let $R$ be a set of vertices of the convex $s$-gon with
vertices $0, 1, \dots, s - 1$. The edges of the polygon with vertex set $R$ are the pairs
$(a, b)$ of elements of $R$ with $a < b$ such that either no element of $R$ lies strictly
between $a$ and $b$, or $a$ is the least and $b$ the greatest element of $R$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 6 (Theorem 6.3).

Formalized by `MetaMathlibExt.inscribedPolygonEdges`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#inscribed-polygon-edges).

## $r$-in-$s$ dissection

Let $D$ be a set of pairs $(a, b)$ of vertices of the convex
$s$-gon with vertices $0, 1, \dots, s - 1$, and let $R$ be a set of its vertices. Then $D$ is
an $r$-in-$s$ dissection with inner polygon $R$ when all of the following hold: the number of
elements of $D$ plus $r$ equals $s$, and $R$ has $r$ elements; every $(a, b) \in D$ is a
diagonal, that is, $a + 2 \le b$ and $(a, b) \ne (0, s - 1)$; no $(a, b)$ and $(c, d)$ in $D$
cross, that is, $a < c < b < d$ never holds; every edge of the polygon with vertex set $R$ is a
side of the $s$-gon, $(a, a + 1)$ or $(0, s - 1)$, or lies in $D$; and every element of $D$
with both endpoints in $R$ is an edge of the polygon with vertex set $R$.

The remaining $s - r$ faces of such a dissection are triangles.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 6 (Definition 6.1).

Formalized by `MetaMathlibExt.IsInnerPolygonDissection`, a definition declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-inner-polygon-dissection).

## Examples of $r$-in-$s$ dissections

For the convex polygons with vertices
$0, 1, \dots, s - 1$: the square ($s = 4$) with no diagonals is a $4$-in-$4$ dissection whose
quadrilateral has all four vertices; the pentagon ($s = 5$) with the single diagonal $(0, 2)$
is a $4$-in-$5$ dissection with quadrilateral on the vertices $0, 2, 3, 4$, but not with
quadrilateral on the vertices $0, 1, 2, 3$.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Section 6 (Definition 6.1).

Formalized by `MetaMathlibExt.isInnerPolygonDissection_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#is-inner-polygon-dissection-examples).

## Descending strictly $k$-Naples parking functions and polygon dissections

Let $n$ and
$k \ge 1$ be natural numbers and let $s = n + k + 1$. Then $s$ times the number of weakly
decreasing preferences of length $n$ that are $k$-Naples but not $(k - 1)$-Naples parking
functions equals the number of triples $(D, R, e)$ such that the set of diagonals $D$ and the
vertex set $R$ form a $(2k + 2)$-in-$s$ dissection of the convex $s$-gon with vertices
$0, \dots, s - 1$, and $e$ is an edge of the inscribed polygon with vertex set $R$.

Rotations of the $s$-gon act freely on these triples, so this says that descending strictly
$k$-Naples parking functions of length $n$ are in bijection with $(2k + 2)$-in-$s$ dissections
up to rotation with a distinguished edge on the $(2k + 2)$-gon.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 6.3 (published as Proposition 6).

Stated but not proved: `MetaMathlibExt.mul_descendingStrictNaplesCount_eq_card_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#mul-descending-strict-naples-count-eq-ca).

## Descending strictly $k$-Naples parking functions and noncrossing partitions

For every
$n$ and every $k \ge 1$, the number of descending strictly $k$-Naples parking functions of
length $n$ (descending preferences that are $k$-Naples but not $(k - 1)$-Naples) equals the
number of noncrossing partitions of $\{0, 1, \dots, n + k\}$ in which the block containing $0$
has exactly $2k + 2$ elements.

## Sources

- J. P. Carvalho, P. E. Harris, G. Rojas Kirby, N. Tripeny and A. R. Vindas Meléndez, *Enumerating k-Naples Parking Functions through Catalan Objects*, INTEGERS 24 (2024), Article A44, Theorem 6.4 (published as Proposition 7).

Stated but not proved: `MetaMathlibExt.descendingStrictNaplesCount_eq_card_noncrossingPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KNaplesParkingWanted.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html#descending-strict-naples-count-eq-card-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-Naples parking functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/k-naples-parking-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/parking-functions/k-naples-parking-functions)
