---
declaration: section
origin: cited
lean: MetaMathlibExt.expected_lucky_spots_weakly_increasing_parking_functions, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.nextFreeSpot, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.parkSpotsFrom, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.parkSpots, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.IsLuckyCar, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.luckyCount, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.q, MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.qInc
statement: formalized
---

# Lucky cars in parking functions

23 results, 11 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html).

## Expected number of lucky cars in weakly increasing parking functions

Let $n \ge 1$. Number
cars and spots from $0$, and encode a weakly increasing parking function of length $n$ as a
nondecreasing map $a : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ with $a(i) \le i$ for every $i$.
The average, over all such maps $a$, of the number of indices $i$ with $a(i) = i$ equals
$\frac{3n}{n+2}$. Here car $i$ parks in spot $i$ and is lucky exactly when $a(i) = i$, so this
number counts both the lucky cars and the lucky spots.

## Sources

- Steve Butler, Kimberly Hadaway, Victoria Lenius, Preston Martens, and Marshall Moats, "Lucky Cars and Lucky Spots in Parking Functions," Journal of Integer Sequences 29 (2026), Article 26.1.1, Corollary, lines 631–633 (supporting lemma lines 619–629), https://cs.uwaterloo.ca/journals/JIS/VOL29/Hadaway/had3.tex The corollary attributes the Dyck-path expectation value to Deutsch.

Formalized by `MetaMathlibExt.expected_lucky_spots_weakly_increasing_parking_functions`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/LuckyParkingFunctions.lean, line 1174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/LuckyParkingFunctions.lean#L1174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#expected-lucky-spots-weakly-increasing-p).

## Next free spot

Number the $n$ spots $0, \dots, n-1$. Given a set $S$ of occupied
spots and a spot $a$, the next free spot is the least spot $s \ge a$ with $s \notin S$; when
every spot $s \ge a$ is occupied, it is $a$ itself.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.nextFreeSpot`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#next-free-spot).

## Greedy parking from an occupied set

Number the $n$ spots $0, \dots, n-1$. Given a list
$a_1, \dots, a_m$ of preferred spots and a set $S$ of occupied spots, cars $1, \dots, m$ arrive in
order and car $k$ takes the least spot at or after $a_k$ that is neither in $S$ nor taken by cars
$1, \dots, k-1$ (or $a_k$ itself if there is none). The result is the list of spots taken, in
arrival order.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.parkSpotsFrom`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#park-spots-from).

## Greedy parking outcome

Let $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ give the
preferred spot of each of $n$ cars. Starting from an empty lot with spots $0, \dots, n-1$, cars
$0, 1, \dots, n-1$ arrive in order, and each takes the least free spot at or after its preference
(or its preference itself if there is none). The outcome sends each car $i$ to the spot it takes.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.parkSpots`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#park-spots).

## Lucky car under greedy parking

Let $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ give the
preferred spot of each of $n$ cars. Cars $0, 1, \dots, n-1$ arrive in order, and each takes the
least spot at or after its preference not taken by an earlier car, or its preferred spot itself
when there is no such spot. Car $i$ is lucky if the spot it takes is its preferred spot $f(i)$.

For a parking function a free spot always exists.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.IsLuckyCar`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#is-lucky-car).

## Number of lucky cars

Let $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ give the preferred
spot of each of $n$ cars, and let cars $0, 1, \dots, n-1$ arrive in order, each taking the least
spot at or after its preference not taken by an earlier car, or its preferred spot itself when
there is no such spot. The number of lucky cars of $f$ is the number of cars $i$ whose spot is
$f(i)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.luckyCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#lucky-count).

## Lucky-car counts

Number the cars and spots $0, \dots, n-1$. For
$i, j \in \{0, \dots, n-1\}$, $q_n(i, j)$ is the number of parking functions
$f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ with $f(i) = j$ in which car $i$ is lucky, that is,
parks in spot $f(i)$.

In the one-based indexing of Butler et al. this is $q_n(i+1, j+1)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.q`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q).

## Increasing lucky-car counts

Number the cars and spots $0, \dots, n-1$. For
$i, j \in \{0, \dots, n-1\}$, $q^{\mathrm{inc}}_n(i, j)$ is the number of weakly increasing parking
functions $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ with $f(i) = j$ in which car $i$ is lucky,
that is, parks in spot $f(i)$.

In the one-based indexing of Butler et al. this is $q^i_n(i+1, j+1)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.qInc`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q-inc).

## Decreasing lucky-car counts

Number the cars and spots $0, \dots, n-1$. For
$i, j \in \{0, \dots, n-1\}$, $q^{\mathrm{dec}}_n(i, j)$ is the number of weakly decreasing parking
functions $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ with $f(i) = j$ in which car $i$ is lucky,
that is, parks in spot $f(i)$.

In the one-based indexing of Butler et al. this is $q^d_n(i+1, j+1)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.qDec`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q-dec).

## Lucky-car polynomial

For $n \in \mathbb{N}$, $f_n \in \mathbb{Q}[x]$ is the polynomial

$$f_n(x) = \frac{1}{n+1} \prod_{i=0}^{n-1} \bigl((n+1-i)\,x + i\bigr).$$

Equivalently, $f_n(x) = \frac{1}{n+1} \prod_{i=1}^{n} \bigl((n+2-i)\,x + (i-1)\bigr)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.luckyGenPoly`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#lucky-gen-poly).

## Parking functions with prescribed lucky and unlucky cars

Number the cars and spots
$0, \dots, n-1$, and let $L$ and $U$ be disjoint sets of cars. The number of parking functions
of length $n$ in which every car in $L$ is lucky and no car in $U$ is lucky equals

$$\prod_{i \in L} (n + 1 - i) \cdot \prod_{i \in U} i \cdot (n + 1)^{n - |L| - |U| - 1},$$

where the power is taken in $\mathbb{Q}$, so the exponent may be negative.

In the paper's numbering of cars from $1$, the factors are $n + 2 - i$ and $i - 1$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Theorem 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.card_parking_lucky_on` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#card-parking-lucky-on).

## Generating polynomial of lucky cars

For $n \in \mathbb{N}$ and $0 \le k \le n$, let $c_k$
be the number of parking functions of length $n$ with exactly $k$ lucky cars. Then in
$\mathbb{Q}[x]$,

$$\frac{1}{n+1} \prod_{i=0}^{n-1} \bigl((n+1-i)x + i\bigr) = \sum_{k=0}^{n} c_k x^k.$$

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Corollary 5.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.luckyGenPoly_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#lucky-gen-poly-eq-sum).

## Factorial moments of the number of lucky cars

Let $n \ge 1$ and $\ell \in \mathbb{N}$, let
$X(f)$ be the number of lucky cars of a parking function $f$ of length $n$, and let
$P_n(x) = \frac{1}{n+1} \prod_{i=0}^{n-1} \bigl((n+1-i)x + i\bigr) \in \mathbb{Q}[x]$. Then

$$\frac{1}{(n+1)^{n-1}} \sum_f X(f)\bigl(X(f)-1\bigr)\cdots\bigl(X(f)-\ell+1\bigr) =
\frac{P_n^{(\ell)}(1)}{(n+1)^{n-1}},$$

where $f$ runs over the parking functions of length $n$ and $P_n^{(\ell)}$ is the $\ell$-th
derivative of $P_n$. Since there are $(n+1)^{n-1}$ parking functions of length $n$, the left side
is the $\ell$-th falling-factorial moment of $X$ for a uniformly random parking function.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Proposition 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.expected_descFactorial_luckyCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#expected-desc-factorial-lucky-count).

## Boundary values of lucky-car counts (Lemma 9)

Let $n \ge 1$, number the cars and spots
$0, \dots, n-1$, and let $q_n(i, j)$ be the number of parking functions of length $n$ in which
car $i$ prefers spot $j$ and is lucky. Then for all $i, j \in \{0, \dots, n-1\}$, with powers
taken in $\mathbb{Q}$ (the integer exponents may be negative),

$$q_n(n-1, j) = \binom{n-1}{j} (j+1)^{j-1} (n-j)^{n-j-2},$$



$$q_n(0, j) = \sum_{k=j+1}^{n} \binom{n-1}{k-1} k^{k-2} (n-k+1)^{n-k-1},$$



$$q_n(i, n-1) = n^{n-2},$$



$$q_n(i, 0) = (n+1)^{n-i-2}\, n^{i-1}\, (2n-i).$$

In the one-based indexing of the source, car $i$ and spot $j$ here are car $i+1$ and spot $j+1$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Lemma 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.q_boundary_values` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q-boundary-values).

## Number of parking functions in which a given car is lucky

Number cars and spots
$0, \dots, n-1$, and let $q_n(i, j)$ be the number of parking functions of length $n$ in which
car $i$ prefers spot $j$ and parks there. Then for every $n$ and every car $i < n$,

$$\sum_{j=0}^{n-1} q_n(i, j) = (n + 1 - i)(n + 1)^{n-2},$$

an identity in $\mathbb{Q}$ (for $n = 1$ the exponent is $-1$). The left side is the number of
parking functions of length $n$ in which car $i$ is lucky; in the paper's one-based numbering
the count for the $i$-th car is $(n + 2 - i)(n + 1)^{n-2}$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Corollary 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.sum_q_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#sum-q-eq).

## Number of parking functions in which the second spot is lucky

Number cars and spots
$0, \dots, n-1$, and let $q_n(i, j)$ be the number of parking functions of length $n$ in which
car $i$ prefers spot $j$ and parks there. Then for every $n \ge 2$, in $\mathbb{Q}$,

$$\sum_{i=0}^{n-1} q_n(i, 1) = \frac{3}{4}(n + 1)^{n-1} - \frac{1}{4}(n - 1)^{n-1}.$$

Since at most one car parks in spot $1$, the left side is the number of parking functions of
length $n$ in which the second spot is lucky, that is, the car parking there preferred it.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Theorem 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.sum_q_second_spot` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#sum-q-second-spot).

## Increasing lucky-car counts (Lemma 18)

Number the cars and spots $0, \dots, n-1$, let
$q^{\mathrm{inc}}_n(i, j)$ be the number of weakly increasing parking functions of length $n$ in
which car $i$ prefers spot $j$ and is lucky, and let $C_m$ be the $m$-th Catalan number. For all
$i, j \in \{0, \dots, n-1\}$, $q^{\mathrm{inc}}_n(i, j) = C_i \, C_{n-i}$ if $i = j$, and
$q^{\mathrm{inc}}_n(i, j) = 0$ otherwise.

In the one-based indexing of the source the diagonal value reads $C_{i-1} C_{n-i+1}$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Lemma 18.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.qInc_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q-inc-eq).

## Ballot paths

For $k, \ell \in \mathbb{N}$, a ballot path to $(k, \ell)$ is a word of length
$k + \ell$ in up steps and right steps with exactly $\ell$ up steps such that every prefix has at
least as many up steps as right steps; equivalently, a lattice path from $(0,0)$ to $(k, \ell)$
with unit up and right steps that stays on or above the line $y = x$.

Formalized by `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.BallotPath`, a definition declared in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#ballot-path).

## Number of ballot paths

For natural numbers $k \le \ell$, the number of lattice paths
from $(0,0)$ to $(k, \ell)$ with unit up and right steps that stay on or above the line $y = x$
is $\frac{\ell - k + 1}{\ell + 1} \binom{k + \ell}{k}$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Lemma 21.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.card_ballotPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#card-ballot-path).

## Decreasing lucky-car counts (Lemma 22)

Number the cars and spots $0, \dots, n-1$, and let
$q^{\mathrm{dec}}_n(i, j)$ be the number of weakly decreasing parking functions of length $n$ in
which car $i$ prefers spot $j$ and is lucky. For all $i, j \in \{0, \dots, n-1\}$, if $i + j < n$
then

$$q^{\mathrm{dec}}_n(i, j) = \frac{(n-i-j)^2}{(n-i)(n-j)} \binom{n-i+j-1}{j} \binom{n-j+i-1}{i},$$

and $q^{\mathrm{dec}}_n(i, j) = 0$ otherwise.

In the one-based indexing of the source the condition reads $i + j \le n + 1$.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Lemma 22.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.qDec_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#q-dec-eq).

## Lucky spots of weakly decreasing parking functions as a sum

Number the cars and spots
$0, \dots, n-1$. For cars $i$ and spots $j$, let $q^d_n(i, j)$ be the number of weakly decreasing
parking functions $f$ of length $n$ (that is, $f(0) \ge f(1) \ge \dots \ge f(n-1)$) with
$f(i) = j$ in which car $i$ is lucky. Then for every spot $j$,

$$\sum_{i=0}^{n-1} q^d_n(i, j) = \sum_{i=1}^{n-j} \frac{(n-i-j+1)^2}{(n+1-i)(n-j)}
\binom{n-i+j}{j} \binom{n-j+i-2}{i-1}.$$

The left side counts the weakly decreasing parking functions in which spot $j$ is lucky, that
is, taken by a car that prefers it.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Corollary 23.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.card_dec_lucky_spot_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#card-dec-lucky-spot-eq-sum).

## Lucky spots of weakly decreasing parking functions as a Catalan convolution

Number the
cars and spots $0, \dots, n-1$. For cars $i$ and spots $j$, let $q^d_n(i, j)$ be the number of
weakly decreasing parking functions $f$ of length $n$ (that is, $f(0) \ge f(1) \ge \dots \ge
f(n-1)$) with $f(i) = j$ in which car $i$ is lucky. Then for every spot $j$,

$$\sum_{i=0}^{n-1} q^d_n(i, j) = \sum_{k=0}^{n-j-1} C_{n-1-k} \, C_k,$$

where $C_m$ is the $m$-th Catalan number.

The left side counts the weakly decreasing parking functions in which spot $j$ is lucky, that
is, taken by a car that prefers it.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Theorem 24.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.card_dec_lucky_spot_eq_sum_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#card-dec-lucky-spot-eq-sum-catalan).

## Expected number of lucky cars in weakly decreasing parking functions

For $n \ge 1$, the
sum of the numbers of lucky cars over all weakly decreasing parking functions $f$ of length $n$
(those with $f(0) \ge f(1) \ge \dots \ge f(n-1)$), divided by the Catalan number $C_n$, equals
$\frac{n+1}{2}$.

There are $C_n$ weakly decreasing parking functions of length $n$, so this is the expected number
of lucky cars, which equals the expected number of lucky spots.

## Sources

- Steve Butler et al., "Lucky Cars and Lucky Spots in Parking Functions", Theorem 25.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.LuckyCarsWanted.expected_lucky_dec` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LuckyCarsWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html#expected-lucky-dec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucky cars in parking functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/parking-functions/lucky-cars-in-parking-functions)
