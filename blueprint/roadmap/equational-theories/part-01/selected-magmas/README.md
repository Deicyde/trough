# Selected magmas

Each magma can be used to establish anti-implications: if $\Gamma$ is the set of all laws satisfied by a magma $G$, then we have $\neg E \leq E'$ whenever $E \in \Gamma$ and $E' \not \in \Gamma$. Large numbers of implications can already be obtained from

- All magmas of size at most $4$, up to isomorphism (of which [there are $178\,985\,294$](https://oeis.org/A001329));
- All commutative magmas of size $5$, up to isomorphism (of which [there are $254\,429\,900$](https://oeis.org/A001425));
- Cyclic groups $\mathbb{Z}/N\mathbb{Z}$ with $2 \leq N \leq 12$ and $x \diamond y = ax^2+bxy+cy^2+dx+ey$ for randomly chosen $a,b,c,d,e$.
- There are only [$1411$ quasigroups of size $5$](https://oeis.org/A057991) (up to isomorphism), and Mace4 can generate all of them in under 20 seconds. A shell script to do this is available [here](https://github.com/zaklogician/equational_theories/tree/cancellative_magmas/scripts/cancellative_magmas). A magma is a quasigroup if, for all $y$, the left/right multiplications $x\mapsto y\diamond x$ and $x\mapsto x\diamond y$ are bijective (equivalent to injective in a finite magma).

We also note that a systematic (computer-assisted) study of magmas of size $3$ was performed in (Berman and Burris 1996), though with current computational resources it was feasible to iterate over all magmas of size up to $4$ by a brute force approach.

Some other magmas have been used to establish counterexamples:

- The cyclic group $\mathbb{Z}/6\mathbb{Z}$ with the addition law.
- The natural numbers with law $x \diamond y = x+1$.
- The natural numbers with law $x \diamond y = xy+1$.
- The reals with $x \diamond y = (x+y)/2$.
- The natural numbers with $x \diamond y$ equal to $x$ when $x=y$ and $x+1$ otherwise.
- The set of strings with $x \diamond y$ equal to $y$ when $x=y$ or when $x$ ends with $yyy$, or $xy$ otherwise (see [this Zulip thread](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/topic/3102.20does.20not.20imply.203176/near/474656031)).
- Vector spaces ${\mathbb F}_2^n$ over ${\mathbb F}_2$, which satisfy [E1571](https://teorth.github.io/equational_theories/implications/?1571) (and hence all the subsequent laws mentioned in [Consequences of 1571](../implications-between-selected-laws/1571-impl.md)).
- Knuth's construction (Knuth 1970) of a central groupoid ([E168](https://teorth.github.io/equational_theories/implications/?168)) as follows. Let $S$ be a (finite) set with a distinguished element $0$, and a binary operation $*$ such that $x*0=0$ and $0*x=x$ for all $x$, and for each $x,y$ there is a unique $z$ with $x*z=y$. One can then define a central groupoid on $S \times S$ by defining $(a,b) \diamond (c,d)$ to equal $(b,c)$ if $c,d \neq 0$; $(b,e)$ if $b*e=c$ is non-zero and $d=0$; and $(a*b,0)$ if $c=0$. One such example in (Knuth 1970) is when $S = \{0,1,2\}$ with $1*1=2*1=2$ and $1*2=2*2=1$.
- Cancellative magmas of sizes 7 to 9, found by hand-guided search using various solvers.
- Two magmas of cardinality $8$ were [constructed by Z3](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/topic/using.20z3/near/474918100).
- A large number of ad-hoc finite magmas were constructed using the Vampire theorem prover. In some cases, inputting theoretical information is useful: see [this discussion](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Outstanding.20equations.2C.20v1/near/478066872).
- Linear magmas $x\diamond y = ax+by$ on various fields, such as ${\mathbb F}_p$ for small primes $p$, have also been used to establish counterexamples. One such choice is $(p,a,b) = (11,1,7)$. See [this discussion](https://leanprover.zulipchat.com/#narrow/stream/458659-Equational/topic/An.20old.20new.20idea). For a noncommutative example, see [this discussion](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Outstanding.20equations.2C.20v1/near/477928995.2E01). For a more systematic exploration of the implications that can be obtained by both commutative and noncommutative linear models, see [this discussion](https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Non-commutative.20linear.20implications).
- A variation of the translation-invariant magma construction which resolved the Asterix / Obelix anti-implication is used to show that [E1661](https://teorth.github.io/equational_theories/implications/?1661) does not imply [E1657](https://teorth.github.io/equational_theories/implications/?1657).
