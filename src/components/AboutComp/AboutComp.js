// components/About.js
import React from 'react';

const AboutComp = () => {
    return (
        <div className="about-container">
            <div className="jumbotron bg-light">
                <h1 className="display-4">מערכת למידה</h1>
                <p className="lead">בית חולים המשפחה הקדושה - נצרת</p>
            </div>
            <div className="container">
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <br/>
                        <h4> המערכת</h4>
                        <p>אנחנו מספקים מערכת לניהול ומעקב אחרי הלומדות הרשומות על עובדי בית החולים</p>
                    </div>
                    
                </div>
            </div>
        </div>
    );
};

export default AboutComp;