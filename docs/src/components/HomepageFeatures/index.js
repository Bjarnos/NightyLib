import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/easy_to_use.png').default,
    description: (
      <>
        NightyLib is a lightweight library that can be installed
        at runtime.
      </>
    ),
  },
  {
    title: 'Most OP Tools',
    Svg: require('@site/static/img/most_op.png').default,
    description: (
      <>
        NightyLib provides powerful tools for coding in Nighty.
        See the <a href="/docs/intro"><code>docs</code></a> for more information.
      </>
    ),
  },
  {
    title: 'Feature Suggestions',
    Svg: require('@site/static/img/community_driven.png').default,
    description: (
      <>
        NightyLib is community-driven! You don't need to
        join a Discord server, suggest features <a href="https://github.com/Bjarnos/NightyLib/issues"
        target='_blank' rel='noopener noreferrer'>here</a>.
      </>
    ),
  },
  {
    title: 'Fast',
    Svg: require('@site/static/img/fast_speed.png').default,
    description: (
      <>
        NightyLib is written in <a href="https://cython.org/">Cython</a> instead of
        standard Python, achieving up to 6x the speed!
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--3')}>
      <div className="text--center">
        <img src={Svg} />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
